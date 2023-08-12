tests/ui/reify-intrinsic.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(core_intrinsics, intrinsics)]

fn a() {
    let _: unsafe extern "rust-intrinsic" fn(isize) -> usize = std::mem::transmute;
    //~^ ERROR cannot coerce
}

fn b() {
    let _ = std::mem::transmute as unsafe extern "rust-intrinsic" fn(isize) -> usize;
    //~^ ERROR casting
}

fn c() {
    let _ = [
        std::intrinsics::likely,
        std::intrinsics::unlikely,
        //~^ ERROR cannot coerce
    ];
}

fn main() {}


