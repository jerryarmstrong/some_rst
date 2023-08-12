tests/ui/dst/dst-rvalue.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that dynamically sized rvalues are forbidden

pub fn main() {
    let _x: Box<str> = Box::new(*"hello world");
    //~^ ERROR E0277

    let array: &[isize] = &[1, 2, 3];
    let _x: Box<[isize]> = Box::new(*array);
    //~^ ERROR E0277
}


