tests/ui/implicit-method-bind.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _f = 10i32.abs; //~ ERROR attempted to take value of method
}


