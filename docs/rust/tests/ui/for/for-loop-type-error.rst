tests/ui/for/for-loop-type-error.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let x = () + (); //~ ERROR cannot add `()` to `()`

    // this shouldn't have a flow-on error:
    for _ in x {}
}


