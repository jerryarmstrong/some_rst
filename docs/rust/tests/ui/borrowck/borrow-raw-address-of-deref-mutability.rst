tests/ui/borrowck/borrow-raw-address-of-deref-mutability.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `&raw mut` cannot be used to turn a `&T` into a `*mut T`.

#![feature(raw_ref_op)]

fn raw_reborrow() {
    let x = &0;

    let q = &raw mut *x;                //~ ERROR cannot borrow
}

unsafe fn raw_reborrow_of_raw() {
    let x = &0 as *const i32;

    let q = &raw mut *x;                //~ ERROR cannot borrow
}

fn main() {}


