tests/ui/opeq.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let mut x: isize = 1;
    x *= 2;
    println!("{}", x);
    assert_eq!(x, 2);
    x += 3;
    println!("{}", x);
    assert_eq!(x, 5);
    x *= x;
    println!("{}", x);
    assert_eq!(x, 25);
    x /= 5;
    println!("{}", x);
    assert_eq!(x, 5);
}


