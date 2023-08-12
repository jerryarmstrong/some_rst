shank-idl/tests/fixtures/instructions/single_file/instruction_with_docs.rs
==========================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig, desc = "The creator of the thing")]
    #[account(1, name = "thing", mut, desc = "The thing to create")]
    CreateThing,
    #[account(
        name = "original_creator",
        sig,
        docs = "The original creator of the thing"
    )]
    CloseThing,
}


