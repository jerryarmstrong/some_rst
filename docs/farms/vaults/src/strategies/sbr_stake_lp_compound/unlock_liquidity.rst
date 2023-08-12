vaults/src/strategies/sbr_stake_lp_compound/unlock_liquidity.rs
===============================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Unlock Liquidity in the Vault instruction handler

use {
    crate::traits::UnlockLiquidity,
    solana_farm_sdk::{instruction::vault::VaultInstruction, vault::Vault},
    solana_program::{
        account_info::AccountInfo, entrypoint::ProgramResult, msg, program_error::ProgramError,
    },
};

impl UnlockLiquidity for VaultInstruction {
    fn unlock_liquidity(_vault: &Vault, _accounts: &[AccountInfo], _amount: u64) -> ProgramResult {
        msg!("Error: Liquidity Unlock is not required for this Vault");
        Err(ProgramError::InvalidArgument)
    }
}


