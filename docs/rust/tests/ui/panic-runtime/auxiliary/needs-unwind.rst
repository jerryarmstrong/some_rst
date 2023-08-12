tests/ui/panic-runtime/auxiliary/needs-unwind.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=unwind
// no-prefer-dynamic

#![crate_type = "rlib"]
#![no_std]
#![feature(c_unwind)]

extern "C-unwind" fn foo() {}

fn bar() {
    let ptr: extern "C-unwind" fn() = foo;
    ptr();
}


