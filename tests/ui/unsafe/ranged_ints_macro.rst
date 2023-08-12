tests/ui/unsafe/ranged_ints_macro.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![feature(rustc_attrs)]

macro_rules! apply {
    ($val:expr) => {
        #[rustc_layout_scalar_valid_range_start($val)]
        #[repr(transparent)]
        pub(crate) struct NonZero<T>(pub(crate) T);
    }
}

apply!(1);

fn main() {
    let _x = unsafe { NonZero(1) };
}


