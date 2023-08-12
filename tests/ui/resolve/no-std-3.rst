tests/ui/resolve/no-std-3.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![no_std]

extern crate std;

mod foo {
    pub fn test() -> Option<i32> {
        Some(2)
    }
}

fn main() {
    let a = core::option::Option::Some("foo");
    a.unwrap();
    foo::test().unwrap();
}


