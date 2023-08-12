tests/ui/regions/regions-simple.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let mut x: isize = 3;
    let y: &mut isize = &mut x;
    *y = 5;
    println!("{}", *y);
}


