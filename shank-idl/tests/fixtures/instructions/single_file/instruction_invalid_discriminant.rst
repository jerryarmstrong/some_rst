shank-idl/tests/fixtures/instructions/single_file/instruction_invalid_discriminant.rs
=====================================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig)]
    CreateThing = 256, // u8::MAX + 1,
}


