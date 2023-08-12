tests/ui/consts/ptr_is_null.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib
// check-pass

#![feature(const_ptr_is_null)]

const FOO: &usize = &42;

pub const _: () = assert!(!(FOO as *const usize).is_null());

pub const _: () = assert!(!(42 as *const usize).is_null());

pub const _: () = assert!((0 as *const usize).is_null());

pub const _: () = assert!(std::ptr::null::<usize>().is_null());

pub const _: () = assert!(!("foo" as *const str).is_null());


