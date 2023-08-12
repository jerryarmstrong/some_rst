tests/ui/single-use-lifetime/zero-uses-in-fn.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

// Test that we DO warn when lifetime name is not used at all.

#![deny(unused_lifetimes)]
#![allow(dead_code, unused_variables)]

fn september<'a>() {}
//~^ ERROR lifetime parameter `'a` never used
//~| HELP elide the unused lifetime

fn october<'a, 'b, T>(s: &'b T) -> &'b T {
    //~^ ERROR lifetime parameter `'a` never used
    //~| HELP elide the unused lifetime
    s
}

fn november<'a, 'b>(s: &'a str) -> &'a str {
    //~^ ERROR lifetime parameter `'b` never used
    //~| HELP elide the unused lifetime
    s
}

fn main() {}


