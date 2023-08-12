tests/ui/parser/impl-item-const-semantic-fail.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct X;

impl X {
    const Y: u8; //~ ERROR associated constant in `impl` without body
}


