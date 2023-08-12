shank-idl/tests/fixtures/instructions/single_file/instruction_with_multiple_args.rs
===================================================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankInstruction)]
pub enum Instruction {
    #[account(0, name = "creator", sig)]
    CloseThing(Option<u8>, ComplexArgs, ComplexArgs),
}


