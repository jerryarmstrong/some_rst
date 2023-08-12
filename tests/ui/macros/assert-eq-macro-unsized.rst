tests/ui/macros/assert-eq-macro-unsized.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    assert_eq!([1, 2, 3][..], vec![1, 2, 3][..]);
}


