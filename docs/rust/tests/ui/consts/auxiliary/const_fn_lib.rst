tests/ui/consts/auxiliary/const_fn_lib.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Crate that exports a const fn. Used for testing cross-crate.

#![crate_type="rlib"]

pub const fn foo() -> usize { 22 }

pub const fn bar() -> fn() {
    fn x() {}
    x
}

#[inline]
pub const fn bar_inlined() -> fn() {
    fn x() {}
    x
}

#[inline(always)]
pub const fn bar_inlined_always() -> fn() {
    fn x() {}
    x
}


