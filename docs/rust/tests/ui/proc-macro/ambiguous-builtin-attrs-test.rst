tests/ui/proc-macro/ambiguous-builtin-attrs-test.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:builtin-attrs.rs
// compile-flags:--test

#![feature(decl_macro, test)]

extern crate test;
extern crate builtin_attrs;
use builtin_attrs::{test, bench};

#[test] // OK, shadowed
fn test() {}

#[bench] // OK, shadowed
fn bench(b: &mut test::Bencher) {}

fn not_main() {
    Test;
    Bench;
    NonExistent; //~ ERROR cannot find value `NonExistent` in this scope
}


