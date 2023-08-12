farm-sdk/src/traits.rs
======================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    use crate::string::ArrayString64;
use solana_program::program_error::ProgramError;

pub trait Named {
    fn name(&self) -> ArrayString64;
}

pub trait Packed {
    fn get_size(&self) -> usize;

    fn pack(&self, output: &mut [u8]) -> Result<usize, ProgramError>;

    fn to_vec(&self) -> Result<Vec<u8>, ProgramError>;

    fn unpack(input: &[u8]) -> Result<Self, ProgramError>
    where
        Self: Sized;
}

pub trait Versioned {
    fn version(&self) -> u16;
}


