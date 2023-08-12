tests/ui/never_type/call-fn-never-arg-wrong-type.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can't pass other types for !

#![feature(never_type)]

fn foo(x: !) -> ! {
    x
}

fn main() {
    foo("wow"); //~ ERROR mismatched types
}


