tests/ui/unsafe/ranged_ints_const.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![feature(rustc_attrs)]

#[rustc_layout_scalar_valid_range_start(1)]
#[repr(transparent)]
pub(crate) struct NonZero<T>(pub(crate) T);
fn main() {}

const fn foo() -> NonZero<u32> { NonZero(0) }
//~^ ERROR initializing type with `rustc_layout_scalar_valid_range` attr is unsafe

const fn bar() -> NonZero<u32> { unsafe { NonZero(0) } }


