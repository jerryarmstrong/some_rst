tests/ui/pptypedef.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn let_in<T, F>(x: T, f: F) where F: FnOnce(T) {}

fn main() {
    let_in(3u32, |i| { assert!(i == 3i32); });
    //~^ ERROR mismatched types
    //~| expected `u32`, found `i32`

    let_in(3i32, |i| { assert!(i == 3u32); });
    //~^ ERROR mismatched types
    //~| expected `i32`, found `u32`
}


