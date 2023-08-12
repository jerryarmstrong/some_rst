tests/ui/feature-gates/feature-gate-custom_mir.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

extern crate core;

#[custom_mir(dialect = "built")] //~ ERROR the `#[custom_mir]` attribute is just used for the Rust test suite
pub fn foo(_x: i32) -> i32 {
    0
}

fn main() {
    assert_eq!(2, foo(2));
}


