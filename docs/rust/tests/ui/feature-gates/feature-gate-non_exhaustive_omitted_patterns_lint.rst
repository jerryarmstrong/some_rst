tests/ui/feature-gates/feature-gate-non_exhaustive_omitted_patterns_lint.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![deny(non_exhaustive_omitted_patterns)]
//~^ WARNING unknown lint: `non_exhaustive_omitted_patterns`
//~| WARNING unknown lint: `non_exhaustive_omitted_patterns`
#![allow(non_exhaustive_omitted_patterns)]
//~^ WARNING unknown lint: `non_exhaustive_omitted_patterns`
//~| WARNING unknown lint: `non_exhaustive_omitted_patterns`

fn main() {
    enum Foo {
        A, B, C,
    }

    #[allow(non_exhaustive_omitted_patterns)]
    //~^ WARNING unknown lint: `non_exhaustive_omitted_patterns`
    //~| WARNING unknown lint: `non_exhaustive_omitted_patterns`
    //~| WARNING unknown lint: `non_exhaustive_omitted_patterns`
    //~| WARNING unknown lint: `non_exhaustive_omitted_patterns`
    match Foo::A {
        Foo::A => {}
        Foo::B => {}
    }
    //~^^^^ ERROR non-exhaustive patterns: `Foo::C` not covered

    match Foo::A {
        Foo::A => {}
        Foo::B => {}
        #[warn(non_exhaustive_omitted_patterns)]
        _ => {}
    }
    //~^^^ WARNING unknown lint: `non_exhaustive_omitted_patterns`
    //~| WARNING unknown lint: `non_exhaustive_omitted_patterns`
}


