src/audit.rs
============

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    crate::{
        config::Config,
        report::Report,
        token::{DelegateBurn, DelegateChange, DelegateTransfer, OwnerChange, TokenAccountEntry},
    },
    solana_client::rpc_client::GetConfirmedSignaturesForAddress2Config,
    solana_sdk::{clock::Slot, pubkey::Pubkey, signature::Signature, signer::Signer},
    solana_transaction_status::{
        EncodedTransaction, EncodedTransactionWithStatusMeta, UiInstruction, UiMessage,
        UiParsedInstruction, UiTransactionEncoding,
    },
    std::str::FromStr,
};

fn get_as_pubkey(json_value: &serde_json::Value, field_name: &str) -> Pubkey {
    Pubkey::from_str(json_value.get(field_name).unwrap().as_str().unwrap()).unwrap()
}

fn try_to_recognize_and_consume_ix(
    current_owner: Pubkey,
    reported_token_address: Pubkey,
    _reported_token_mint: Pubkey,
    token_account_entry: &mut TokenAccountEntry,
    slot: Slot,
    sig: Signature,
    ix: &serde_json::Value,
) -> bool {
    const CONSUMED: bool = false;
    const IGNORED: bool = false;

    match ix.get("type").as_ref() {
        Some(serde_json::value::Value::String(ix_type)) => {
            let ix_info = ix.get("info");
            match ix_type.as_ref() {
                "transfer" | "transferChecked" => {
                    let source_address = get_as_pubkey(ix_info.unwrap(), "source");
                    let destination_address = get_as_pubkey(ix_info.unwrap(), "destination");
                    if source_address != reported_token_address
                        && destination_address != reported_token_address
                    {
                        // irrelevant transfer instruction (ixes can be mixed arbitrarily)
                        return IGNORED;
                    }

                    if source_address != reported_token_address {
                        assert_eq!(destination_address, reported_token_address);
                        // transfer incoming into reported_token_address isn't harmful
                        return IGNORED;
                    }

                    let signer = get_as_pubkey(ix_info.unwrap(), "authority");
                    // anything signed off by current owner isn't harmful
                    if signer == current_owner {
                        return IGNORED;
                    }

                    // unrelated mint; well no-checked ixes doens't have mint....
                    //dbg!(&ix);
                    //let mint = get_as_pubkey(ix_info.unwrap(), "mint");
                    //if mint != reported_token_mint {
                    //    return IGNORED;
                    //}

                    let original_ix = format!("{}", ix).replace("\"", "\"\"");
                    let original_ix = format!("\"{}\"", original_ix);
                    token_account_entry
                        .possible_delegate_transfers
                        .push(DelegateTransfer {
                            slot,
                            transaction_id: sig,
                            signer,
                            // TODO: todo: properly handle this field!
                            amount: format!(
                                "{}",
                                ix_info
                                    .unwrap()
                                    .get("tokenAmount")
                                    .map(|ta| ta.get("uiAmountString").unwrap())
                                    .unwrap_or_else(|| ix_info.unwrap().get("amount").unwrap())
                            ),
                            original_ix,
                        });
                    CONSUMED
                }
                "burn" | "burnChecked" => {
                    let token_address = get_as_pubkey(ix_info.unwrap(), "account");
                    if token_address != reported_token_address {
                        // unrelated burns
                        return IGNORED;
                    }

                    let original_ix = format!("{}", ix).replace("\"", "\"\"");
                    let original_ix = format!("\"{}\"", original_ix);
                    token_account_entry
                        .possible_delegate_burns
                        .push(DelegateBurn {
                            slot,
                            transaction_id: sig,
                            signer: get_as_pubkey(ix_info.unwrap(), "authority"),
                            // TODO: todo: properly handle this field!
                            amount: format!(
                                "{}",
                                ix_info
                                    .unwrap()
                                    .get("tokenAmount")
                                    .map(|ta| ta.get("uiAmountString").unwrap())
                                    .unwrap_or_else(|| ix_info.unwrap().get("amount").unwrap())
                            ),
                            original_ix,
                        });
                    CONSUMED
                }
                "approve" | "approveChecked" => {
                    let signer = get_as_pubkey(ix_info.unwrap(), "owner");
                    // anything signed off by current owner isn't harmful
                    if signer == current_owner {
                        return IGNORED;
                    }

                    let token_address = get_as_pubkey(ix_info.unwrap(), "source");
                    if token_address != reported_token_address {
                        // unrelated approvals
                        return IGNORED;
                    }

                    let original_ix = format!("{}", ix).replace("\"", "\"\"");
                    let original_ix = format!("\"{}\"", original_ix);
                    let new_delegate = get_as_pubkey(ix_info.unwrap(), "delegate");
                    token_account_entry
                        .all_delegate_addresses
                        .insert(new_delegate);
                    token_account_entry.delegate_changes.push(DelegateChange {
                        slot,
                        transaction_id: sig,
                        signer,
                        new_delegate,
                        original_ix,
                    });
                    CONSUMED
                }
                "setAuthority" => {
                    match (ix_info.map(|info| info.get("authorityType").unwrap())).as_ref() {
                        Some(serde_json::value::Value::String(authority_type)) => {
                            match authority_type.as_ref() {
                                "accountOwner" => {
                                    let signer = get_as_pubkey(ix_info.unwrap(), "authority");
                                    // anything signed off by current owner isn't harmful
                                    if signer == current_owner {
                                        return IGNORED;
                                    }

                                    let token_address = get_as_pubkey(ix_info.unwrap(), "account");
                                    if token_address != reported_token_address {
                                        // unrelated authorizations
                                        return IGNORED;
                                    }

                                    let original_ix = format!("{}", ix).replace("\"", "\"\"");
                                    let original_ix = format!("\"{}\"", original_ix);
                                    token_account_entry.owner_changes.push(OwnerChange {
                                        slot,
                                        transaction_id: sig,
                                        new_owner: get_as_pubkey(ix_info.unwrap(), "newAuthority"),
                                        signer,
                                        original_ix,
                                    });
                                    CONSUMED
                                }
                                "closeAccount" => CONSUMED,
                                _ => !CONSUMED,
                            }
                        }
                        _ => !CONSUMED,
                    }
                }
                "initializeAccount" | "closeAccount" => IGNORED,
                "mintTo" | "mintToChecked" => IGNORED,
                "revoke" => IGNORED, // TODO: this could be useful to create a nicely-looking post-incident report?
                _ => !CONSUMED,
            }
        }
        _ => !CONSUMED,
    }
}

pub fn run(config: Config, owners: Vec<Box<dyn Signer>>, mints: Option<Vec<Pubkey>>) {
    println!("audit");
    let mut report = Report::new();
    const SIGNATURES_LIMIT: usize = 1000;
    crate::for_all_spl_token_accounts(
        &config,
        owners.as_slice(),
        mints.as_deref(),
        |config, owner, reported_token_address, account| {
            let rpc_client = &config.rpc_client;
            let owner_pubkey = owner.pubkey();
            let mut token_account_entry = report
                .entries_by_token_address
                //.entry((owner_pubkey, account.mint))
                .entry(*reported_token_address)
                .or_insert_with(|| TokenAccountEntry::new(owner_pubkey, account.mint));
            let mut before = Option::<Signature>::None;
            loop {
                let request_config = GetConfirmedSignaturesForAddress2Config {
                    before,
                    limit: Some(SIGNATURES_LIMIT),
                    ..GetConfirmedSignaturesForAddress2Config::default()
                };
                #[allow(deprecated)]
                let sigs = rpc_client
                    .get_confirmed_signatures_for_address2_with_config(
                        reported_token_address,
                        request_config,
                    )
                    .unwrap();

                before = if sigs.len() < SIGNATURES_LIMIT {
                    None
                } else {
                    sigs.last()
                        .and_then(|s| Signature::from_str(s.signature.as_str()).ok())
                };

                // Exclude any transactions which failed
                let total_sig_len = sigs.len();
                token_account_entry.total_tx_count += total_sig_len;
                let sigs = sigs.iter().filter_map(|sig_with_status| {
                    if sig_with_status.err.is_some() {
                        None
                    } else {
                        Signature::from_str(sig_with_status.signature.as_str()).ok()
                    }
                });
                token_account_entry.failed_tx_count += total_sig_len - sigs.clone().count();

                for sig in sigs {
                    #[allow(deprecated)]
                    let confirmation = rpc_client
                        .get_confirmed_transaction(&sig, UiTransactionEncoding::JsonParsed)
                        .unwrap();
                    let slot = confirmation.slot;
                    let EncodedTransactionWithStatusMeta { transaction, meta } =
                        confirmation.transaction;
                    let inner_ix = meta.and_then(|meta| {
                        meta.inner_instructions
                            .map(|ixs| ixs.into_iter().map(|ixs| ixs.instructions).flatten())
                    });
                    let mut instructions =
                        if let EncodedTransaction::Json(transaction) = transaction {
                            if let UiMessage::Parsed(message) = transaction.message {
                                message.instructions
                            } else {
                                Vec::new()
                            }
                        } else {
                            Vec::new()
                        };

                    if let Some(inner_ix) = inner_ix {
                        instructions.extend(inner_ix);
                    }

                    // only spl token instructions will be parsed
                    let mut new_ix_in_tx = true;
                    instructions
                        .into_iter()
                        .filter_map(|ix| {
                            if let UiInstruction::Parsed(UiParsedInstruction::Parsed(instruction)) =
                                ix
                            {
                                let program_id =
                                    Pubkey::from_str(instruction.program_id.as_str()).unwrap();
                                if program_id == spl_token::id() {
                                    Some((program_id, instruction.parsed))
                                } else {
                                    None
                                }
                            } else {
                                None
                            }
                        })
                        // program_id must be the tokenkeg according the previous .filter_map()
                        .filter(|(_program_id, ix)| {
                            if new_ix_in_tx {
                                new_ix_in_tx = false;
                                token_account_entry.scanned_tx_count += 1;
                            }
                            token_account_entry.scanned_spl_token_ix_count += 1;
                            try_to_recognize_and_consume_ix(
                                owner_pubkey,
                                *reported_token_address,
                                account.mint,
                                &mut token_account_entry,
                                slot,
                                sig,
                                ix,
                            )
                        })
                        .for_each(|(program_id, ix)| {
                            dbg!(("unknown instruction!", program_id, ix));
                            panic!();
                        });
                }

                // last
                if before.is_none() {
                    break;
                }
            }
        },
    )
    .unwrap();

    report.summary(std::io::stdout()).unwrap();
    println!();
    report.detail(std::io::stdout()).unwrap();
}


