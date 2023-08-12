src/main.rs
===========

Last edited: 2023-02-04 18:21:00

Contents:

.. code-block:: rs

    use mpl_token_auth_rules::{
    instruction::{
        builders::{CreateOrUpdateBuilder, WriteToBufferBuilder},
        CreateOrUpdateArgs, InstructionBuilder, WriteToBufferArgs,
    },
    state::{CompareOp, Rule, RuleSetV1},
};
use rmp_serde::Serializer;
use serde::Serialize;

use solana_client::rpc_client::RpcClient;
use solana_sdk::compute_budget::ComputeBudgetInstruction;
use solana_sdk::{
    native_token::LAMPORTS_PER_SOL, pubkey, pubkey::Pubkey, signature::Signer,
    signer::keypair::Keypair, transaction::Transaction,
};
use std::fmt::Display;
use std::fs;

// --------------------------------
// Define Program Allow List
// --------------------------------
const ROOSTER_PROGRAM_ID: Pubkey = pubkey!("Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz");
const TOKEN_METADATA_PROGRAM_ID: Pubkey = pubkey!("metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s");
const TRANSFER_PROGRAM_ALLOW_LIST: [Pubkey; 2] = [TOKEN_METADATA_PROGRAM_ID, ROOSTER_PROGRAM_ID];
const DELEGATE_PROGRAM_ALLOW_LIST: [Pubkey; 2] = [TOKEN_METADATA_PROGRAM_ID, ROOSTER_PROGRAM_ID];
const ADVANCED_DELEGATE_PROGRAM_ALLOW_LIST: [Pubkey; 2] =
    [TOKEN_METADATA_PROGRAM_ID, ROOSTER_PROGRAM_ID];

// --------------------------------
// RuleSet operations and scenarios
// from token-metadata
// --------------------------------
// Type from token-metadata.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum TransferScenario {
    Holder,
    TransferDelegate,
    SaleDelegate,
    MigrationDelegate,
    WalletToWallet,
}

impl Display for TransferScenario {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Holder => write!(f, "Owner"),
            Self::TransferDelegate => write!(f, "TransferDelegate"),
            Self::SaleDelegate => write!(f, "SaleDelegate"),
            Self::MigrationDelegate => write!(f, "MigrationDelegate"),
            Self::WalletToWallet => write!(f, "WalletToWallet"),
        }
    }
}

// Type from token-metadata.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum UpdateScenario {
    MetadataAuth,
    Delegate,
    Proxy,
}

impl Display for UpdateScenario {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            UpdateScenario::MetadataAuth => write!(f, "MetadataAuth"),
            UpdateScenario::Delegate => write!(f, "Delegate"),
            UpdateScenario::Proxy => write!(f, "Proxy"),
        }
    }
}

// Type from token-metadata.
#[repr(C)]
#[derive(PartialEq, Eq, Debug, Clone, Copy)]
pub enum MetadataDelegateRole {
    Authority,
    Collection,
    Use,
    Update,
}

#[repr(C)]
#[derive(PartialEq, Eq, Debug, Clone, Copy)]
pub enum TokenDelegateRole {
    Sale,
    Transfer,
    Utility,
    Staking,
    Standard,
    LockedTransfer,
    Migration = 255,
}

// Type from token-metadata.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum DelegateScenario {
    Metadata(MetadataDelegateRole),
    Token(TokenDelegateRole),
}

impl Display for DelegateScenario {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let message = match self {
            Self::Metadata(role) => match role {
                MetadataDelegateRole::Authority => "Authority".to_string(),
                MetadataDelegateRole::Collection => "Collection".to_string(),
                MetadataDelegateRole::Use => "Use".to_string(),
                MetadataDelegateRole::Update => "Update".to_string(),
            },
            Self::Token(role) => match role {
                TokenDelegateRole::Sale => "Sale".to_string(),
                TokenDelegateRole::Transfer => "Transfer".to_string(),
                TokenDelegateRole::LockedTransfer => "LockedTransfer".to_string(),
                TokenDelegateRole::Utility => "Utility".to_string(),
                TokenDelegateRole::Staking => "Staking".to_string(),
                _ => panic!("Invalid delegate role"),
            },
        };

        write!(f, "{message}")
    }
}

// Type from token-metadata.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Operation {
    Transfer { scenario: TransferScenario },
    Update { scenario: UpdateScenario },
    Delegate { scenario: DelegateScenario },
}

impl ToString for Operation {
    fn to_string(&self) -> String {
        match self {
            Self::Transfer { scenario } => format!("Transfer:{}", scenario),
            Self::Update { scenario } => format!("Update:{}", scenario),
            Self::Delegate { scenario } => format!("Delegate:{}", scenario),
        }
    }
}

// Payload key type from token-metadata.
#[repr(C)]
#[derive(PartialEq, Eq, Debug, Clone)]
pub enum PayloadKey {
    Amount,
    Authority,
    AuthoritySeeds,
    Delegate,
    DelegateSeeds,
    Destination,
    DestinationSeeds,
    Holder,
    Source,
    SourceSeeds,
}

impl ToString for PayloadKey {
    fn to_string(&self) -> String {
        match self {
            PayloadKey::Amount => "Amount",
            PayloadKey::Authority => "Authority",
            PayloadKey::AuthoritySeeds => "AuthoritySeeds",
            PayloadKey::Delegate => "Delegate",
            PayloadKey::DelegateSeeds => "DelegateSeeds",
            PayloadKey::Destination => "Destination",
            PayloadKey::DestinationSeeds => "DestinationSeeds",
            PayloadKey::Holder => "Holder",
            PayloadKey::Source => "Source",
            PayloadKey::SourceSeeds => "SourceSeeds",
        }
        .to_string()
    }
}

struct ComposedRules {
    transfer_rule: Rule,
    wallet_to_wallet_rule: Rule,
    delegate_rule: Rule,
    advanced_delegate_rule: Rule,
}

// Get the four Composed Rules used in this RuleSet.
fn get_composed_rules() -> ComposedRules {
    // --------------------------------
    // Create Primitive Rules
    // --------------------------------
    let nft_amount = Rule::Amount {
        field: PayloadKey::Amount.to_string(),
        amount: 1,
        operator: CompareOp::Eq,
    };

    let source_program_allow_list = Rule::ProgramOwnedList {
        programs: TRANSFER_PROGRAM_ALLOW_LIST.to_vec(),
        field: PayloadKey::Source.to_string(),
    };

    let dest_program_allow_list = Rule::ProgramOwnedList {
        programs: TRANSFER_PROGRAM_ALLOW_LIST.to_vec(),
        field: PayloadKey::Destination.to_string(),
    };

    let authority_program_allow_list = Rule::ProgramOwnedList {
        programs: TRANSFER_PROGRAM_ALLOW_LIST.to_vec(),
        field: PayloadKey::Authority.to_string(),
    };

    let source_is_wallet = Rule::IsWallet {
        field: PayloadKey::Source.to_string(),
    };

    let dest_is_wallet = Rule::IsWallet {
        field: PayloadKey::Destination.to_string(),
    };

    let delegate_program_allow_list = Rule::ProgramOwnedList {
        programs: DELEGATE_PROGRAM_ALLOW_LIST.to_vec(),
        field: PayloadKey::Delegate.to_string(),
    };

    let advanced_delegate_program_allow_list = Rule::ProgramOwnedList {
        programs: ADVANCED_DELEGATE_PROGRAM_ALLOW_LIST.to_vec(),
        field: PayloadKey::Delegate.to_string(),
    };

    // --------------------------------
    // Create Composed Rules from
    // Primitive Rules
    // --------------------------------
    // amount is 1 && (source owner on allow list || dest owner on allow list || authority owner on allow list )
    let transfer_rule = Rule::All {
        rules: vec![
            nft_amount.clone(),
            Rule::Any {
                rules: vec![
                    source_program_allow_list,
                    dest_program_allow_list,
                    authority_program_allow_list,
                ],
            },
        ],
    };

    // (amount is 1 && source is wallet && dest is wallet)
    let wallet_to_wallet_rule = Rule::All {
        rules: vec![nft_amount.clone(), source_is_wallet, dest_is_wallet],
    };

    let delegate_rule = Rule::All {
        rules: vec![nft_amount.clone(), delegate_program_allow_list],
    };

    let advanced_delegate_rule = Rule::All {
        rules: vec![nft_amount, advanced_delegate_program_allow_list],
    };

    ComposedRules {
        transfer_rule,
        wallet_to_wallet_rule,
        delegate_rule,
        advanced_delegate_rule,
    }
}

// Read a keypair from a file path.
pub fn read_keypair(path: &String) -> Keypair {
    let secret_string: String = fs::read_to_string(path).expect("Could not get path from string");

    // Try to decode the secret string as a JSON array of ints first and then as a base58 encoded string to support Phantom private keys.
    let secret_bytes: Vec<u8> = match serde_json::from_str(&secret_string) {
        Ok(bytes) => bytes,
        Err(_) => panic!("Could not deserialize string"),
    };

    Keypair::from_bytes(&secret_bytes).unwrap()
}

fn main() {
    let url = "https://api.devnet.solana.com".to_string();
    let rpc_client = RpcClient::new(url);
    let payer = read_keypair(&("keypair/devnet-test-rule-set-8.json".to_string()));
    let signature = rpc_client
        .request_airdrop(&payer.pubkey(), LAMPORTS_PER_SOL)
        .unwrap();

    loop {
        let confirmed = rpc_client.confirm_transaction(&signature).unwrap();
        if confirmed {
            break;
        }
    }

    // --------------------------------
    // Create RuleSet
    // --------------------------------
    // Find RuleSet PDA.
    let rule_set_name = "Metaplex Royalty RuleSet Dev".to_string();
    let (rule_set_addr, _ruleset_bump) =
        mpl_token_auth_rules::pda::find_rule_set_address(payer.pubkey(), rule_set_name.clone());
    println!("{}: {}", rule_set_name, rule_set_addr);

    // Create a RuleSet.
    let mut royalty_rule_set = RuleSetV1::new(rule_set_name, payer.pubkey());

    // Get transfer and wallet-to-wallet rules.
    let rules = get_composed_rules();

    // --------------------------------
    // Set up transfer operations
    // --------------------------------
    let transfer_owner_operation = Operation::Transfer {
        scenario: TransferScenario::Holder,
    };

    let transfer_transfer_delegate_operation = Operation::Transfer {
        scenario: TransferScenario::TransferDelegate,
    };

    let transfer_sale_delegate_operation = Operation::Transfer {
        scenario: TransferScenario::SaleDelegate,
    };

    let transfer_migration_delegate_operation = Operation::Transfer {
        scenario: TransferScenario::MigrationDelegate,
    };

    let transfer_wallet_to_wallet_operation = Operation::Transfer {
        scenario: TransferScenario::WalletToWallet,
    };

    royalty_rule_set
        .add(
            transfer_owner_operation.to_string(),
            rules.transfer_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            transfer_transfer_delegate_operation.to_string(),
            rules.transfer_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            transfer_sale_delegate_operation.to_string(),
            rules.transfer_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            transfer_migration_delegate_operation.to_string(),
            rules.transfer_rule,
        )
        .unwrap();
    royalty_rule_set
        .add(
            transfer_wallet_to_wallet_operation.to_string(),
            rules.wallet_to_wallet_rule,
        )
        .unwrap();

    // --------------------------------
    // Setup metadata delegate operations
    // --------------------------------
    let metadata_delegate_authority_operation = Operation::Delegate {
        scenario: DelegateScenario::Metadata(MetadataDelegateRole::Authority),
    };

    let metadata_delegate_collection_operation = Operation::Delegate {
        scenario: DelegateScenario::Metadata(MetadataDelegateRole::Collection),
    };

    let metadata_delegate_use_operation = Operation::Delegate {
        scenario: DelegateScenario::Metadata(MetadataDelegateRole::Use),
    };

    let metadata_delegate_update_operation = Operation::Delegate {
        scenario: DelegateScenario::Metadata(MetadataDelegateRole::Update),
    };

    royalty_rule_set
        .add(
            metadata_delegate_authority_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            metadata_delegate_collection_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            metadata_delegate_use_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            metadata_delegate_update_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();

    // --------------------------------
    // Setup token delegate operations
    // --------------------------------
    let token_delegate_sale_operation = Operation::Delegate {
        scenario: DelegateScenario::Token(TokenDelegateRole::Sale),
    };

    let token_delegate_transfer_operation = Operation::Delegate {
        scenario: DelegateScenario::Token(TokenDelegateRole::Transfer),
    };

    let token_delegate_locked_transfer_operation = Operation::Delegate {
        scenario: DelegateScenario::Token(TokenDelegateRole::LockedTransfer),
    };

    let token_delegate_utility_operation = Operation::Delegate {
        scenario: DelegateScenario::Token(TokenDelegateRole::Utility),
    };

    let token_delegate_staking_operation = Operation::Delegate {
        scenario: DelegateScenario::Token(TokenDelegateRole::Staking),
    };

    royalty_rule_set
        .add(
            token_delegate_sale_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();
    royalty_rule_set
        .add(
            token_delegate_transfer_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();

    // --------------------------------
    // NOTE THIS IS THE ONLY OPERATION
    // THAT USES THE ADVANCED DELEGATE
    // RULE.
    // --------------------------------
    royalty_rule_set
        .add(
            token_delegate_locked_transfer_operation.to_string(),
            rules.advanced_delegate_rule,
        )
        .unwrap();

    royalty_rule_set
        .add(
            token_delegate_utility_operation.to_string(),
            rules.delegate_rule.clone(),
        )
        .unwrap();

    royalty_rule_set
        .add(
            token_delegate_staking_operation.to_string(),
            rules.delegate_rule,
        )
        .unwrap();

    println!("{:#?}", royalty_rule_set);

    // --------------------------------
    // Put RuleSet on chain
    // --------------------------------
    // Serialize the RuleSet using RMP serde.
    let mut serialized_rule_set = Vec::new();
    royalty_rule_set.clone()
        .serialize(&mut Serializer::new(&mut serialized_rule_set))
        .unwrap();
    let json = serde_json::to_string(&royalty_rule_set).unwrap();
    println!("{}", json);
    // We need to write this RuleSet in chunks.
    let (buffer_pda, _buffer_bump) = mpl_token_auth_rules::pda::find_buffer_address(payer.pubkey());

    let mut overwrite = true;
    for serialized_rule_set_chunk in serialized_rule_set.chunks(500) {
        // Create a `write to buffer` instruction.
        let buffer_ix = WriteToBufferBuilder::new()
            .payer(payer.pubkey())
            .buffer_pda(buffer_pda)
            .build(WriteToBufferArgs::V1 {
                serialized_rule_set: serialized_rule_set_chunk.to_vec(),
                overwrite,
            })
            .unwrap()
            .instruction();

        // Add it to a transaction.
        let latest_blockhash = rpc_client.get_latest_blockhash().unwrap();
        let buffer_tx = Transaction::new_signed_with_payer(
            &[buffer_ix],
            Some(&payer.pubkey()),
            &[&payer],
            latest_blockhash,
        );

        println!("TX Length: {:?}", buffer_tx.message.serialize().len());
        assert!(
            buffer_tx.message.serialize().len() <= 1232,
            "Transaction exceeds packet limit of 1232"
        );

        // Send and confirm transaction.
        let signature = rpc_client.send_and_confirm_transaction(&buffer_tx).unwrap();
        println!("Buffer tx signature: {}", signature);

        if overwrite {
            overwrite = false;
        }
    }

    // Create a `create` instruction.
    let create_ix = CreateOrUpdateBuilder::new()
        .payer(payer.pubkey())
        .rule_set_pda(rule_set_addr)
        .buffer_pda(buffer_pda)
        .build(CreateOrUpdateArgs::V1 {
            serialized_rule_set: vec![],
        })
        .unwrap()
        .instruction();

    // Increase compute budget for this one.
    let compute_budget_ix = ComputeBudgetInstruction::set_compute_unit_limit(400_000);

    // Add it to a transaction.
    let latest_blockhash = rpc_client.get_latest_blockhash().unwrap();
    let create_tx = Transaction::new_signed_with_payer(
        &[compute_budget_ix, create_ix],
        Some(&payer.pubkey()),
        &[&payer],
        latest_blockhash,
    );

    // Check size.
    assert!(
        create_tx.message.serialize().len() <= 1232,
        "Transaction exceeds packet limit of 1232"
    );

    // Send and confirm transaction.
    let signature = rpc_client.send_and_confirm_transaction(&create_tx).unwrap();
    println!("Create tx signature: {}", signature);
}


