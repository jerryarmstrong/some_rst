tests/ui/unsafe/ranged_ints2_const.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#![feature(rustc_attrs)]

#[rustc_layout_scalar_valid_range_start(1)]
#[repr(transparent)]
pub(crate) struct NonZero<T>(pub(crate) T);
fn main() {
}

const fn foo() -> NonZero<u32> {
    let mut x = unsafe { NonZero(1) };
    let y = &mut x.0; //~ ERROR mutable references
    //~^ ERROR mutation of layout constrained field is unsafe
    unsafe { NonZero(1) }
}

const fn bar() -> NonZero<u32> {
    let mut x = unsafe { NonZero(1) };
    let y = unsafe { &mut x.0 }; //~ ERROR mutable references
    unsafe { NonZero(1) }
}

const fn boo() -> NonZero<u32> {
    let mut x = unsafe { NonZero(1) };
    unsafe { let y = &mut x.0; } //~ ERROR mutable references
    unsafe { NonZero(1) }
}


