tests/run-make-fulldeps/mixing-deps/prog.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate dylib;
extern crate both;

use std::mem;

fn main() {
    assert_eq!(unsafe { mem::transmute::<&isize, usize>(&both::foo) },
               dylib::addr());
}


