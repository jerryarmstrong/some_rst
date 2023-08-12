tests/ui/unboxed-closures/unboxed-closures-type-mismatch.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::FnMut;

pub fn main() {
    let mut f = |x: isize, y: isize| -> isize { x + y };
    let z = f(1_usize, 2);    //~ ERROR mismatched types
    println!("{}", z);
}


