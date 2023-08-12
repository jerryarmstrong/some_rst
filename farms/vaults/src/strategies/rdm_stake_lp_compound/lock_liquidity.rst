farms/vaults/src/strategies/rdm_stake_lp_compound/lock_liquidity.rs
===================================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    //! Lock Liquidity in the Vault instruction handler

use {
    crate::traits::LockLiquidity,
    solana_farm_sdk::{instruction::vault::VaultInstruction, vault::Vault},
    solana_program::{
        account_info::AccountInfo, entrypoint::ProgramResult, msg, program_error::ProgramError,
    },
};

impl LockLiquidity for VaultInstruction {
    fn lock_liquidity(_vault: &Vault, _accounts: &[AccountInfo], _amount: u64) -> ProgramResult {
        msg!("Error: Liquidity Lock is not required for this Vault");
        Err(ProgramError::InvalidArgument)
    }
}


