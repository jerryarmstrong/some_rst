tests/ui/numbers-arithmetic/div-mod.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




pub fn main() {
    let x: isize = 15;
    let y: isize = 5;
    assert_eq!(x / 5, 3);
    assert_eq!(x / 4, 3);
    assert_eq!(x / 3, 5);
    assert_eq!(x / y, 3);
    assert_eq!(15 / y, 3);
    assert_eq!(x % 5, 0);
    assert_eq!(x % 4, 3);
    assert_eq!(x % 3, 0);
    assert_eq!(x % y, 0);
    assert_eq!(15 % y, 0);
}


