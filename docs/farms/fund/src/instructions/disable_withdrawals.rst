fund/src/instructions/disable_withdrawals.rs
============================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Fund DisableWithdrawals instruction handler

use {
    crate::fund_info::FundInfo,
    solana_farm_sdk::fund::Fund,
    solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, msg},
};

pub fn disable_withdrawals(
    _fund: &Fund,
    fund_info: &mut FundInfo,
    _accounts: &[AccountInfo],
) -> ProgramResult {
    msg!("Disable withdrawals from the Fund");

    fund_info.set_withdrawal_start_time(0)?;
    fund_info.set_withdrawal_end_time(0)?;
    fund_info.set_withdrawal_approval_required(true)
}


