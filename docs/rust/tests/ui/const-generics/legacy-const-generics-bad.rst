tests/ui/const-generics/legacy-const-generics-bad.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:legacy-const-generics.rs

extern crate legacy_const_generics;

fn foo<const N: usize>() {
    let a = 1;
    legacy_const_generics::foo(0, a, 2);
    //~^ ERROR attempt to use a non-constant value in a constant

    legacy_const_generics::foo(0, N, 2);

    legacy_const_generics::foo(0, N + 1, 2);
    //~^ ERROR generic parameters may not be used in const operations
}

fn main() {}


