tests/ui/lint/redundant-semicolon/item-stmt-semi.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(redundant_semicolons)]

fn main() {
    fn inner() {}; //~ ERROR unnecessary
    struct Bar {}; //~ ERROR unnecessary
}


