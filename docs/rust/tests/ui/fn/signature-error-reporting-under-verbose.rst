tests/ui/fn/signature-error-reporting-under-verbose.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zverbose

fn foo(_: i32, _: i32) {}

fn needs_ptr(_: fn(i32, u32)) {}
//~^ NOTE function defined here
//~| NOTE

fn main() {
    needs_ptr(foo);
    //~^ ERROR mismatched types
    //~| NOTE expected `u32`, found `i32`
    //~| NOTE expected fn pointer `fn(i32, u32)`
    //~| NOTE arguments to this function are incorrect
}


