src/lib.rs
==========

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    crate::config::Config,
    solana_account_decoder::UiAccountEncoding,
    solana_client::{
        client_error::Result as ClientResult,
        rpc_config::{RpcAccountInfoConfig, RpcProgramAccountsConfig},
        rpc_filter::{Memcmp, MemcmpEncodedBytes, RpcFilterType},
    },
    solana_sdk::{program_pack::Pack, pubkey::Pubkey, signer::Signer},
};

pub mod audit;
pub mod cleanup;
pub mod config;
pub mod report;
pub mod token;

pub fn for_all_spl_token_accounts<F>(
    config: &Config,
    wallets: &[Box<dyn Signer>],
    mints: Option<&[Pubkey]>,
    mut f: F,
) -> ClientResult<()>
where
    F: FnMut(&Config, &dyn Signer, &Pubkey, &spl_token::state::Account),
{
    let mut already_processed = std::collections::HashSet::new();

    for wallet in wallets {
        let wallet_pubkey = wallet.pubkey();
        if already_processed.contains(&wallet_pubkey) {
            continue;
        } else {
            already_processed.insert(wallet_pubkey);
        }

        let filters = Some(vec![
            RpcFilterType::DataSize(spl_token::state::Account::LEN as u64),
            RpcFilterType::Memcmp(Memcmp {
                offset: 32,
                bytes: MemcmpEncodedBytes::Binary(bs58::encode(wallet_pubkey).into_string()),
                encoding: None,
            }),
        ]);
        let account_config = RpcAccountInfoConfig {
            encoding: Some(UiAccountEncoding::Base64),
            ..RpcAccountInfoConfig::default()
        };
        let get_program_accounts_config = RpcProgramAccountsConfig {
            filters,
            account_config,
            ..RpcProgramAccountsConfig::default()
        };

        config
            .rpc_client
            .get_program_accounts_with_config(&spl_token::id(), get_program_accounts_config)?
            .into_iter()
            .filter_map(|(addr, acct)| {
                let token_account = spl_token::state::Account::unpack(&acct.data).ok();
                if token_account.is_none() {
                    eprintln!("unexpected account data at {}:", addr);
                }
                Some(addr).zip(token_account)
            })
            .filter(|(_address, account)| {
                mints
                    .map(|mints| mints.contains(&account.mint))
                    .unwrap_or(true)
            })
            .map(|(address, account)| (config, wallet.as_ref(), address, account))
            .for_each(|(config, wallet, address, account)| f(config, wallet, &address, &account));
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_client::rpc_client::RpcClient;
    use solana_sdk::signer::null_signer::NullSigner;
    use std::str::FromStr;

    #[test]
    fn test_for_all_spl_token_accounts() {
        let json_rpc_url = "https://api.mainnet-beta.solana.com".to_string();
        let rpc_client = RpcClient::new(json_rpc_url.clone());
        let fee_payer = Box::new(NullSigner::new(
            &Pubkey::from_str("EriSViggFFQ72fYgCKYyattiY3rDsx9bnMgMUpGa5x2H").unwrap(),
        ));
        let config = Config {
            json_rpc_url,
            rpc_client,
            fee_payer,
            dry_run: true,
            verbose: true,
        };
        let wallet = NullSigner::new(
            &Pubkey::from_str("EriSViggFFQ72fYgCKYyattiY3rDsx9bnMgMUpGa5x2H").unwrap(),
        );
        let mint = Pubkey::from_str("4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R").unwrap();
        for_all_spl_token_accounts(
            &config,
            &[Box::new(wallet)],
            Some(&[mint]),
            |_config, wallet, address, account| {
                println!(
                    "owner: {}\naddress: {}\naccount: {:?}",
                    wallet.pubkey(),
                    address,
                    account
                );
            },
        )
        .unwrap();
    }
}


