router-saber/src/user_init.rs
=============================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Initialize a new user for a Saber farm instruction

use {
    solana_farm_sdk::program::account,
    solana_program::{
        account_info::AccountInfo,
        entrypoint::ProgramResult,
        hash::Hasher,
        instruction::{AccountMeta, Instruction},
        msg,
        program::invoke,
        program_error::ProgramError,
        pubkey::Pubkey,
        system_program,
    },
};

pub fn user_init(accounts: &[AccountInfo]) -> ProgramResult {
    msg!("Processing AmmInstruction::UserInit");

    #[allow(clippy::deprecated_cfg_attr)]
    #[cfg_attr(rustfmt, rustfmt_skip)]
    if let [
        funding_account,
        user_account,
        farm_program_id,
        lp_token_mint,
        _spl_token_id,
        _system_program,
        miner,
        miner_vault,
        quarry,
        rewarder
        ] = accounts
    {
        if &quarry_mine::id() != farm_program_id.key {
            return Err(ProgramError::IncorrectProgramId);
        }
        if account::exists(miner)? {
            return Err(ProgramError::AccountAlreadyInitialized);
        }

        let (miner_derived, bump) = Pubkey::find_program_address(
            &[
                b"Miner",
                &quarry.key.to_bytes(),
                &user_account.key.to_bytes(),
            ],
            &quarry_mine::id(),
        );

        if &miner_derived != miner.key {
            msg!("Error: Invalid Miner address");
            return Err(ProgramError::InvalidSeeds);
        }

        let mut hasher = Hasher::default();
        hasher.hash(b"global:create_miner");

        let mut data = hasher.result().as_ref()[..8].to_vec();
        data.push(bump);

        let saber_accounts = vec![
            AccountMeta::new(*funding_account.key, true),
            AccountMeta::new(*miner.key, false),
            AccountMeta::new(*quarry.key, false),
            AccountMeta::new(*rewarder.key, false),
            AccountMeta::new_readonly(system_program::id(), false),
            AccountMeta::new_readonly(*funding_account.key, true),
            AccountMeta::new(*lp_token_mint.key, false),
            AccountMeta::new(*miner_vault.key, false),
            AccountMeta::new_readonly(spl_token::id(), false),
        ];

        let instruction = Instruction {
            program_id: quarry_mine::id(),
            accounts: saber_accounts,
            data,
        };

        invoke(&instruction, accounts)?;
    } else {
        return Err(ProgramError::NotEnoughAccountKeys);
    }

    msg!("AmmInstruction::UserInit complete");
    Ok(())
}


