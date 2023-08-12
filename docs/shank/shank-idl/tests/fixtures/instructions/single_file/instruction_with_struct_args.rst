shank-idl/tests/fixtures/instructions/single_file/instruction_with_struct_args.rs
=================================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig)]
    #[account(1, name = "thing", mut)]
    CreateThing {
        some_args: SomeArgs,
        other_args: OtherArgs,
    },
    #[account(0, name = "creator", sig)]
    CloseThing(Option<u8>),
}


