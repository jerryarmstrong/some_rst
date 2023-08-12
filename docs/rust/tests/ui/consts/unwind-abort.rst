tests/ui/consts/unwind-abort.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(c_unwind, const_extern_fn)]

// We don't unwind in const-eval anyways.
const extern "C" fn foo() {
    panic!()
}

const fn bar() {
    foo();
}

fn main() {
    bar();
}


