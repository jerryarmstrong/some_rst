tests/ui/associated-types/associated-types-issue-21212.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// Regression test for #21212: an overflow occurred during trait
// checking where normalizing `Self::Input` led to normalizing the
// where clauses in the environment which in turn required normalizing
// `Self::Input`.


pub trait Parser {
    type Input;

    fn parse(input: <Self as Parser>::Input) {
        panic!()
    }
}

impl <P> Parser for P {
    type Input = ();
}

fn main() {
}


