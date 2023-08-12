tests/ui/binop/binary-minus-without-space.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that issue #954 stays fixed


pub fn main() {
    match -1 { -1 => {}, _ => panic!("wat") }
    assert_eq!(1-1, 0);
}


