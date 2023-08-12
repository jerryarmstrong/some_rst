tests/ui/consts/const-eval/unwind-abort.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(c_unwind, const_extern_fn)]

const extern "C" fn foo() {
    panic!() //~ ERROR evaluation of constant value failed
}

const _: () = foo();
// Ensure that the CTFE engine handles calls to `extern "C"` aborting gracefully

fn main() {
    let _ = foo();
}


