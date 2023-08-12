src/cleanup.rs
==============

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    crate::config::Config,
    solana_sdk::{
        message::Message, program_option::COption, pubkey::Pubkey, signature::Signer,
        transaction::Transaction,
    },
    spl_token::{self, instruction::revoke, state::Account},
};

fn cleanup(config: &Config, owner: &dyn Signer, address: &Pubkey, account: &Account) {
    if let COption::Some(delegate) = account.delegate {
        println!("revoking delegate {} for account {}", delegate, address);
        let rpc_client = &config.rpc_client;
        let revoke_ix = revoke(&spl_token::id(), address, &owner.pubkey(), &[]).unwrap();
        let fee_payer = config.fee_payer.pubkey();
        let message = Message::new(&[revoke_ix], Some(&fee_payer));
        let (blockhash, fee_calculator) = rpc_client.get_recent_blockhash().unwrap();
        let fee_payer_balance = rpc_client.get_balance(&fee_payer).unwrap();
        let fee = fee_calculator.calculate_fee(&message);
        if !config.dry_run {
            if fee_payer_balance < fee {
                eprintln!("fee payer ({}) insufficient funds!", fee_payer);
                std::process::exit(1);
            }

            let mut transaction = Transaction::new_unsigned(message);
            transaction.sign(&[owner, config.fee_payer.as_ref()], blockhash);

            match rpc_client.send_and_confirm_transaction_with_spinner(&transaction) {
                Ok(txid) => println!("txid: {}", txid),
                Err(error) => eprintln!(
                    "Error revoking delegate {} for account {}: {}",
                    delegate, address, error
                ),
            }
        }
    }
}

pub fn run(config: Config, owners: Vec<Box<dyn Signer>>, mints: Option<Vec<Pubkey>>) {
    println!("cleanup");
    crate::for_all_spl_token_accounts(&config, owners.as_slice(), mints.as_deref(), cleanup)
        .unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_client::rpc_client::RpcClient;
    use solana_sdk::signer::null_signer::NullSigner;
    use spl_token::state::AccountState;
    use std::str::FromStr;

    #[test]
    fn test_cleanup_delegation() {
        let json_rpc_url = "https://api.mainnet-beta.solana.com".to_string();
        let rpc_client = RpcClient::new(json_rpc_url.clone());
        let wallet = NullSigner::new(
            &Pubkey::from_str("EriSViggFFQ72fYgCKYyattiY3rDsx9bnMgMUpGa5x2H").unwrap(),
        );
        let fee_payer = Box::new(NullSigner::new(
            &Pubkey::from_str("EriSViggFFQ72fYgCKYyattiY3rDsx9bnMgMUpGa5x2H").unwrap(),
        ));
        let mint = Pubkey::from_str("4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R").unwrap();
        let delegate = Pubkey::from_str("BaDmyYaaua9k8mZuL53UUt8E6peRMeT3cRVjYcLm68T7").unwrap();
        let config = Config {
            json_rpc_url,
            rpc_client,
            fee_payer,
            dry_run: true,
            verbose: true,
        };
        let account = Account {
            mint,
            owner: wallet.pubkey(),
            amount: 10,
            delegate: COption::Some(delegate),
            state: AccountState::Initialized,
            is_native: COption::None,
            delegated_amount: 999,
            close_authority: COption::None,
        };
        cleanup(&config, &wallet, &mint, &account);
    }
}


