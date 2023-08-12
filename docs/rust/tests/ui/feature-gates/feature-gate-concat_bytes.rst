tests/ui/feature-gates/feature-gate-concat_bytes.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = concat_bytes!(b'A', b"BC"); //~ ERROR use of unstable library feature 'concat_bytes'
    assert_eq!(a, &[65, 66, 67]);
}


