test-program/src/lib.rs
=======================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use saf::AccountPlan;
use saf::Constraints;
use solana_program::program_error::ProgramError;
use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, pubkey::Pubkey,
};
use solana_program::{declare_id, msg};
declare_id!("extw959P4WToez4DkuXwNsJszqGpe3HuY56AcG5yevx");
entrypoint!(process_instruction);
fn process_instruction<'entry>(
    _program_id: &'entry Pubkey,
    accounts: &'entry [AccountInfo<'entry>],
    instruction_data: &'entry [u8],
) -> ProgramResult {
    // An Account plan sets up program validation for all input accounts and lookup table accounts.

    let mut plan = match instruction_data[0] {
        0 => AccountPlan::new(accounts, 3, true),
        1 => AccountPlan::new(accounts, 3, false),
        _ => Err(ProgramError::InvalidInstructionData),
    }?;

    match instruction_data[1] {
        0 => simple_ix(&mut plan, instruction_data),
        1 => optional_account_ix(&mut plan, instruction_data),
        _ => Err(ProgramError::InvalidInstructionData),
    }
}

fn pda_of_this_program_constraint<'a>(seeds: &'a [&[u8]]) -> Constraints<'a> {
    Constraints::pda(seeds, crate::id(), true, true)
}

fn simple_ix(plan: &mut AccountPlan, ix_data: &[u8]) -> ProgramResult {
    let payer = plan.required_account("payer", Constraints::payer())?;
    let seeds = &[b"test".as_ref(), payer.info.key.as_ref(), &ix_data[1..]];
    let subject = plan.required_account("subject", pda_of_this_program_constraint(seeds))?;
    plan.system_program()?;
    plan.validate()?;
    subject.initialize_account(10, &crate::id(), &payer)?;

    Ok(())
}

/// Example of an optional Account
fn optional_account_ix(plan: &mut AccountPlan, ix_data: &[u8]) -> ProgramResult {
    let payer = plan.required_account("payer", Constraints::payer())?;
    plan.system_program()?;
    let seeds = &[b"test".as_ref(), payer.info.key.as_ref(), &ix_data[1..]];
    let subject = plan.optional_account("subject", pda_of_this_program_constraint(seeds))?;
    plan.validate()?;
    if let Some(subject) = subject {
        subject.initialize_account(10, &crate::id(), &payer)?;
    } else {
        msg!("Nothing to do");
    }

    Ok(())
}


