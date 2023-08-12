tests/ui/consts/const-extern-fn/const-extern-fn-requires-unsafe.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![feature(const_extern_fn)]

const unsafe extern "C" fn foo() -> usize { 5 }

fn main() {
    let a: [u8; foo()];
    //[mir]~^ call to unsafe function is unsafe and requires unsafe function or block
    //[thir]~^^ call to unsafe function `foo` is unsafe and requires unsafe function or block
    foo();
    //[mir]~^ ERROR call to unsafe function is unsafe and requires unsafe function or block
}


