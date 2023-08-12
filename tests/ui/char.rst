tests/ui/char.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let c: char = 'x';
    let d: char = 'x';
    assert_eq!(c, 'x');
    assert_eq!('x', c);
    assert_eq!(c, c);
    assert_eq!(c, d);
    assert_eq!(d, c);
    assert_eq!(d, 'x');
    assert_eq!('x', d);
}


