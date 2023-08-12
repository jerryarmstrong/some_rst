tests/ui/macros/issue-34421-mac-expr-bad-stmt-good-add-semi.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! make_item {
    ($a:ident) => {
        struct $a;
    }; //~^ ERROR expected expression
       //~| ERROR expected expression
}

fn a() {
    make_item!(A)
}
fn b() {
    make_item!(B)
}

fn main() {}


