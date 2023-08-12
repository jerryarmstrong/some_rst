tests/ui/type-alias-enum-variants/incorrect-variant-form-through-Self-issue-58006.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Enum {
    A(usize),
}

impl Enum {
    fn foo(&self) -> () {
        match self {
            Self::A => (),
            //~^ ERROR expected unit struct, unit variant or constant, found tuple variant
        }
    }
}

fn main() {}


