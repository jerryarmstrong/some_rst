tests/ui/variance/variance-regions-unused-indirect.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that disallow lifetime parameters that are unused.

enum Foo<'a> { //~ ERROR parameter `'a` is never used
    //~^ ERROR recursive types `Foo` and `Bar` have infinite size
    Foo1(Bar<'a>)
}

enum Bar<'a> { //~ ERROR parameter `'a` is never used
    Bar1(Foo<'a>)
}

fn main() {}


