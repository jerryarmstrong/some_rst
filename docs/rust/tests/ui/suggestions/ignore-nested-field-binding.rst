tests/ui/suggestions/ignore-nested-field-binding.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #88403, where prefixing with an underscore was
// erroneously suggested for a nested shorthand struct field binding.

// run-rustfix
#![allow(unused)]
#![forbid(unused_variables)]

struct Inner { i: i32 }
struct Outer { o: Inner }

fn foo(Outer { o: Inner { i } }: Outer) {}
//~^ ERROR: unused variable: `i`
//~| HELP: try ignoring the field

fn main() {
    let s = Outer { o: Inner { i: 42 } };
    let Outer { o: Inner { i } } = s;
    //~^ ERROR: unused variable: `i`
    //~| HELP: try ignoring the field
}


