tests/ui/parser/impl-item-fn-no-body-semantic-fail.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct X;

impl X {
    fn f(); //~ ERROR associated function in `impl` without body
}


