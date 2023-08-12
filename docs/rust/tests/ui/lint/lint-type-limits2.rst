tests/ui/lint/lint-type-limits2.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![warn(overflowing_literals)]

// compile-flags: -D unused-comparisons
fn main() { }


fn bar() -> i8 {
    return 123;
}

fn baz() -> bool {
    128 > bar() //~ ERROR comparison is useless due to type limits
                //~| WARN literal out of range for `i8`
}


