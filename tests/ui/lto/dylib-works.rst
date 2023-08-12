tests/ui/lto/dylib-works.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// aux-build:dylib.rs

extern crate dylib;

fn main() {
    dylib::foo(1);
}


