tests/ui/generator/print/generator-print-verbose-3.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zverbose

#![feature(generators, generator_trait)]

fn main() {
    let x = "Type mismatch test";
    let generator :() = || {
    //~^ ERROR mismatched types
        yield 1i32;
        return x
    };
}


