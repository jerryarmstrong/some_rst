src/tools/miri/tests/pass/char.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let c = 'x';
    assert_eq!(c, 'x');
    assert!('a' < 'z');
    assert!('1' < '9');
    assert_eq!(std::char::from_u32('x' as u32), Some('x'));
}


