tests/ui/resolve/no-std-2.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![no_std]

extern crate std;

fn main() {
    let a = core::option::Option::Some("foo");
    a.unwrap();
}


