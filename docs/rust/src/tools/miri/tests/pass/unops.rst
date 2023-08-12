src/tools/miri/tests/pass/unops.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(!true, false);
    assert_eq!(!0xFFu16, 0xFF00);
    assert_eq!(-{ 1i16 }, -1i16);
}


