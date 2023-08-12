fund/src/instructions/orca/vault_lock_liquidity.rs
==================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Lock liquidity in the Orca Vault instruction

use {
    crate::{common, fund_info::FundInfo},
    solana_farm_sdk::{fund::Fund, instruction::vault::VaultInstruction},
    solana_program::{
        account_info::AccountInfo,
        entrypoint::ProgramResult,
        instruction::{AccountMeta, Instruction},
        msg,
        program::invoke_signed,
        program_error::ProgramError,
    },
};

pub fn lock_liquidity(fund: &Fund, accounts: &[AccountInfo], amount: u64) -> ProgramResult {
    #[allow(clippy::deprecated_cfg_attr)]
    #[cfg_attr(rustfmt, rustfmt_skip)]
    if let [
        _admin_account,
        fund_metadata,
        fund_info_account,
        fund_authority,
        vault_program_id,
        fund_vault_metadata,
        vault_metadata,
        vault_info_account,
        vault_authority,
        spl_token_program,
        vault_token_mint,
        fund_vault_user_account,
        fund_vt_token_custody,
        vault_reward_custody,
        vault_lp_token_custody,
        farm_program,
        vault_stake_info,
        vault_stake_custody,
        farm_id,
        farm_authority,
        farm_lp_token_mint,
        farm_base_token_vault,
        farm_reward_token_vault,
        ] = accounts
    {
        // validate accounts
        msg!("Validate state and accounts");
        let fund_info = FundInfo::new(fund_info_account);
        if fund_info.get_liquidation_start_time()? > 0 {
            msg!("Error: Fund is in liquidation state");
            return Err(ProgramError::Custom(516));
        }
        if fund_authority.key != &fund.fund_authority {
            msg!("Error: Invalid Fund authority account");
            return Err(ProgramError::Custom(517));
        }

        common::check_unpack_target_vault(
            &fund.fund_program_id,
            vault_program_id.key,
            fund_metadata.key,
            vault_metadata.key,
            fund_vault_metadata,
        )?;

        // prepare instruction and call vault program
        let seeds: &[&[&[u8]]] = &[&[
            b"fund_authority",
            fund.name.as_bytes(),
            &[fund.authority_bump],
        ]];

        let vault_accounts = vec![
            AccountMeta::new_readonly(*fund_authority.key, true),
            AccountMeta::new_readonly(*vault_metadata.key, false),
            AccountMeta::new(*vault_info_account.key, false),
            AccountMeta::new_readonly(*vault_authority.key, false),
            AccountMeta::new_readonly(*spl_token_program.key, false),
            AccountMeta::new(*vault_token_mint.key, false),
            AccountMeta::new(*fund_vault_user_account.key, false),
            AccountMeta::new(*fund_vt_token_custody.key, false),
            AccountMeta::new(*vault_reward_custody.key, false),
            AccountMeta::new(*vault_lp_token_custody.key, false),
            AccountMeta::new_readonly(*farm_program.key, false),
            AccountMeta::new(*vault_stake_info.key, false),
            AccountMeta::new(*vault_stake_custody.key, false),
            AccountMeta::new(*farm_id.key, false),
            AccountMeta::new_readonly(*farm_authority.key, false),
            AccountMeta::new(*farm_lp_token_mint.key, false),
            AccountMeta::new(*farm_base_token_vault.key, false),
            AccountMeta::new(*farm_reward_token_vault.key, false),
        ];

        let instruction = Instruction {
            program_id: *vault_program_id.key,
            accounts: vault_accounts,
            data: VaultInstruction::LockLiquidity { amount }.to_vec()?,
        };

        invoke_signed(&instruction, accounts, seeds)?;

        Ok(())
    } else {
        Err(ProgramError::NotEnoughAccountKeys)
    }
}


