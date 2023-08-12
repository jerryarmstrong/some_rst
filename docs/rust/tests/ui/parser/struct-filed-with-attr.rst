tests/ui/parser/struct-filed-with-attr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue: 100461, Try to give a helpful diagnostic even when the next struct field has an attribute.
// run-rustfix

struct Feelings {
    owo: bool
    //~^ ERROR expected `,`, or `}`, found `#`
    #[allow(unused)]
    uwu: bool,
}

impl Feelings {
    #[allow(unused)]
    fn hmm(&self) -> bool {
        self.owo
    }
}

fn main() { }


