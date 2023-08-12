shank-idl/tests/fixtures/instructions/single_file/instruction_with_optional_account.rs
======================================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig)]
    #[account(1, name = "thing", mut, optional)]
    CreateThing(SomeArgs),
    #[account(name = "creator", sig)]
    CloseThing,
}


