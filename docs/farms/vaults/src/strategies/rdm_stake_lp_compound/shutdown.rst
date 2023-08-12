vaults/src/strategies/rdm_stake_lp_compound/shutdown.rs
=======================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Vault Shutdown instruction handler

use {
    crate::{traits::Shutdown, vault_info::VaultInfo},
    solana_farm_sdk::{instruction::vault::VaultInstruction, vault::Vault},
    solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, msg},
};

impl Shutdown for VaultInstruction {
    fn shutdown(_vault: &Vault, accounts: &[AccountInfo]) -> ProgramResult {
        if let [_admin_account, _vault_metadata, vault_info_account, _multisig_account] = accounts {
            // Don't do anything special on shutdown for this Vault, just disable deposits and withdrawals
            let mut vault_info = VaultInfo::new(vault_info_account);
            msg!("disable_deposit");
            vault_info.disable_deposits()?;
            msg!("disable_withdrawal");
            vault_info.disable_withdrawals()?;
            //pda::close_account(admin_account, vault_info_account)
        }
        Ok(())
    }
}


