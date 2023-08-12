tests/ui/proc-macro/add-impl.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:add-impl.rs

#[macro_use]
extern crate add_impl;

#[derive(AddImpl)]
struct B;

fn main() {
    B.foo();
    foo();
    bar::foo();
}


