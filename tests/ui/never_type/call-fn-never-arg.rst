tests/ui/never_type/call-fn-never-arg.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can use a ! for an argument of type !

// check-pass

#![feature(never_type)]
#![allow(unreachable_code)]

fn foo(x: !) -> ! {
    x
}

fn main() {
    foo(panic!("wowzers!"))
}


