shank-idl/tests/fixtures/instructions/single_file/instruction_no_args.rs
========================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig)]
    #[account(1, name = "thing", mut)]
    CreateThing,
    #[account(name = "original_creator", sig)]
    CloseThing,
}


