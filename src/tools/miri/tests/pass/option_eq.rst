src/tools/miri/tests/pass/option_eq.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(std::char::from_u32('x' as u32), Some('x'));
}


