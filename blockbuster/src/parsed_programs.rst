blockbuster/src/parsed_programs.rs
==================================

Last edited: 2023-06-27 20:46:29

Contents:

.. code-block:: rs

    pub enum Program {
    Bubblegum {
        parser: bubblegum::BubblegumParser,
        instruction_result: BubblegumInstruction,
        account_result: (),
    },
}

impl ProgramParser for Program {}


