shank-idl/tests/fixtures/instructions/single_file/instruction_with_optional_signer_account.rs
=============================================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", signer)]
    #[account(1, name = "thing", writable)]
    CreateThing(SomeArgs),
    #[account(name = "creator", optional_signer)]
    CloseThing,
}


