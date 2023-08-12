tests/run-make-fulldeps/std-core-cycle/foo.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

extern crate bar;

#[global_allocator]
static A: bar::A = bar::A;

#[no_mangle]
pub extern "C" fn a(a: u32, b: u32) -> u32 {
    a / b
}


