tests/ui/macros/assert-ne-macro-unsized.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    assert_ne!([6, 6, 6][..], vec![1, 2, 3][..]);
}


