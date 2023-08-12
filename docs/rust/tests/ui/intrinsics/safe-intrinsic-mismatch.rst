tests/ui/intrinsics/safe-intrinsic-mismatch.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]
#![feature(rustc_attrs)]

extern "rust-intrinsic" {
    fn size_of<T>() -> usize; //~ ERROR intrinsic safety mismatch

    #[rustc_safe_intrinsic]
    fn assume(b: bool); //~ ERROR intrinsic safety mismatch
}

fn main() {}


