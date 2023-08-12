tests/ui/consts/const-ptr-unique.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ptr_internals)]

use std::ptr::Unique;

fn main() {
    let mut i: u32 = 10;
    let unique = Unique::new(&mut i).unwrap();
    let x: &'static *mut u32 = &(unique.as_ptr());
    //~^ ERROR temporary value dropped while borrowed
}


