tests/ui/borrowck/borrow-raw-address-of-deref-mutability-ok.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(raw_ref_op)]

fn raw_reborrow() {
    let x = &0;
    let y = &mut 0;

    let p = &raw const *x;
    let r = &raw const *y;
    let s = &raw mut *y;
}

unsafe fn raw_reborrow_of_raw() {
    let x = &0 as *const i32;
    let y = &mut 0 as *mut i32;

    let p = &raw const *x;
    let r = &raw const *y;
    let s = &raw mut *y;
}

fn main() {}


