tests/ui/cross-crate/cci_impl_exe.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cci_impl_lib.rs

extern crate cci_impl_lib;
use cci_impl_lib::uint_helpers;

pub fn main() {
    //let bt0 = sys::frame_address();
    //println!("%?", bt0);

    3.to(10, |i| {
        println!("{}", i);

        //let bt1 = sys::frame_address();
        //println!("%?", bt1);
        //assert_eq!(bt0, bt1);
    })
}


