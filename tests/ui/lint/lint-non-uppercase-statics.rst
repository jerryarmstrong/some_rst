tests/ui/lint/lint-non-uppercase-statics.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(non_upper_case_globals)]
#![allow(dead_code)]

static foo: isize = 1; //~ ERROR static variable `foo` should have an upper case name

static mut bar: isize = 1; //~ ERROR static variable `bar` should have an upper case name

#[no_mangle]
pub static extern_foo: isize = 1; // OK, because #[no_mangle] supersedes the warning

fn main() { }


