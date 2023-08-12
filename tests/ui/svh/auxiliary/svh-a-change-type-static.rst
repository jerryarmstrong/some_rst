tests/ui/svh/auxiliary/svh-a-change-type-static.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! The `svh-a-*.rs` files are all deviations from the base file
//! svh-a-base.rs with some difference (usually in `fn foo`) that
//! should not affect the strict version hash (SVH) computation
//! (#14132).

#![crate_name = "a"]

macro_rules! three {
    () => { 3 }
}

pub trait U {}
pub trait V {}
impl U for () {}
impl V for () {}

static A_CONSTANT : i32 = 2;

pub fn foo<T:U>(_: isize) -> isize {
    3
}

pub fn an_unused_name() -> isize {
    4
}


