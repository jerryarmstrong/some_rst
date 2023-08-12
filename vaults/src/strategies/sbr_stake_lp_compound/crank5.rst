vaults/src/strategies/sbr_stake_lp_compound/crank5.rs
=====================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Crank step 5 instruction handler

use {
    crate::{strategies::common, vault_info::VaultInfo},
    solana_farm_sdk::{
        program::{account, protocol::saber},
        vault::{Vault, VaultStrategy},
    },
    solana_program::{
        account_info::AccountInfo, entrypoint::ProgramResult, msg, program_error::ProgramError,
    },
};

pub fn crank5(vault: &Vault, accounts: &[AccountInfo]) -> ProgramResult {
    #[allow(clippy::deprecated_cfg_attr)]
    #[cfg_attr(rustfmt, rustfmt_skip)]
    if let [
        _funding_account,
        _vault_metadata,
        vault_info_account,
        vault_authority,
        spl_token_program,
        lp_token_custody,
        farm_program,
        vault_stake_info,
        vault_miner_account,
        quarry,
        rewarder
        ] = accounts
    {
        // validate accounts
        if vault_authority.key != &vault.vault_authority ||
           !account::check_token_account_owner(vault_miner_account, vault_stake_info.key)?
        {
            msg!("Error: Invalid Vault accounts");
            return Err(ProgramError::InvalidArgument);
        }
        if let VaultStrategy::StakeLpCompoundRewards {
            farm_id: farm_id_key,
            lp_token_custody: lp_token_custody_key,
            vault_stake_info: vault_stake_info_key,
            ..
        } = vault.strategy
        {
            if &farm_id_key != quarry.key {
                msg!("Error: Invalid farm id");
                return Err(ProgramError::InvalidArgument);
            }
            if &vault_stake_info_key != vault_stake_info.key {
                msg!("Error: Invalid Vault Stake Info account");
                return Err(ProgramError::InvalidArgument);
            }
            if &lp_token_custody_key != lp_token_custody.key {
                msg!("Error: Invalid custody accounts");
                return Err(ProgramError::InvalidArgument);
            }
        } else {
            msg!("Error: Vault strategy mismatch");
            return Err(ProgramError::InvalidArgument);
        }

        let vault_info = VaultInfo::new(vault_info_account);
        common::check_min_crank_interval(&vault_info)?;

        // read balances
        let lp_token_balance = account::get_token_balance(lp_token_custody)?;
        msg!("Read balances. lp_token_balance: {}", lp_token_balance,);
        if lp_token_balance == 0 {
            msg!("Nothing to do: Not enough LP tokens to stake");
            return Ok(());
        }

        let seeds: &[&[&[u8]]] = &[&[
            b"vault_authority",
            vault.name.as_bytes(),
            &[vault.authority_bump],
        ]];

        msg!("Stake LP tokens");
        saber::stake_with_seeds(
            &[
                vault_authority.clone(),
                lp_token_custody.clone(),
                farm_program.clone(),
                spl_token_program.clone(),
                vault_stake_info.clone(),
                vault_miner_account.clone(),
                quarry.clone(),
                rewarder.clone(),
            ],
            seeds,
            lp_token_balance,
        )?;

        Ok(())
    } else {
        Err(ProgramError::NotEnoughAccountKeys)
    }
}


