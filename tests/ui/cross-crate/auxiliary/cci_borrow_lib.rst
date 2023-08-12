tests/ui/cross-crate/auxiliary/cci_borrow_lib.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo(x: &usize) -> usize {
    *x
}


