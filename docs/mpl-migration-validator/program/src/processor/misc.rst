program/src/processor/misc.rs
=============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use super::*;

pub fn init_signer(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let payer_info = next_account_info(account_info_iter)?;
    let program_signer_info = next_account_info(account_info_iter)?;
    let system_program_info = next_account_info(account_info_iter)?;

    let bump = assert_derivation(
        program_id,
        program_signer_info,
        &[b"signer"],
        MigrationError::InvalidSignerDerivation,
    )?;
    let signer_seeds: &[&[u8]] = &[b"signer", &[bump]];

    if system_program_info.key != &solana_program::system_program::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Already initialized
    if !program_signer_info.data.borrow().is_empty() {
        return Err(MigrationError::AlreadyInitialized.into());
    }

    let signer = ProgramSigner { bump };

    let serialized_data = signer.try_to_vec()?;
    let data_len = serialized_data.len();

    mpl_utils::create_or_allocate_account_raw(
        *program_id,
        program_signer_info,
        system_program_info,
        payer_info,
        data_len,
        signer_seeds,
    )?;

    sol_memcpy(
        &mut program_signer_info.data.borrow_mut(),
        serialized_data.as_slice(),
        data_len,
    );

    Ok(())
}


