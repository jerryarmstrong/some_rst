shank-idl/tests/fixtures/instructions/single_file/instruction_invalid_attr.rs
=============================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    // Misspelled sig
    #[account(0, name = "creator", sg)]
    CreateThing,
}


