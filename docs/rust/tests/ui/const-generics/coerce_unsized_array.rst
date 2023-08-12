tests/ui/const-generics/coerce_unsized_array.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn foo<const N: usize>(v: &[u8; N]) -> &[u8] {
    v
}

fn main() {
    assert_eq!(foo(&[1, 2]), &[1, 2]);
}


