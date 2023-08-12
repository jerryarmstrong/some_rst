fund/src/instructions/set_withdrawal_schedule.rs
================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Fund SetWithdrawalSchedule instruction handler

use {
    crate::fund_info::FundInfo,
    solana_farm_sdk::fund::{Fund, FundSchedule},
    solana_program::{
        account_info::AccountInfo, entrypoint::ProgramResult, msg, program_error::ProgramError,
    },
};

pub fn set_withdrawal_schedule(
    _fund: &Fund,
    fund_info: &mut FundInfo,
    _accounts: &[AccountInfo],
    schedule: &FundSchedule,
) -> ProgramResult {
    msg!("Update Fund withdrawal parameters");
    if schedule.start_time >= schedule.end_time {
        msg!("Error: start_time must be less than end_time");
        return Err(ProgramError::Custom(514));
    }

    fund_info.set_withdrawal_start_time(schedule.start_time)?;
    fund_info.set_withdrawal_end_time(schedule.end_time)?;
    fund_info.set_withdrawal_approval_required(schedule.approval_required)?;
    fund_info.set_withdrawal_min_amount_usd(schedule.min_amount_usd)?;
    fund_info.set_withdrawal_max_amount_usd(schedule.max_amount_usd)?;
    fund_info.set_withdrawal_fee(schedule.fee)
}


