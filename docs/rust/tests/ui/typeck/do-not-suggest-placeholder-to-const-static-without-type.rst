tests/ui/typeck/do-not-suggest-placeholder-to-const-static-without-type.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const A; //~ ERROR missing type for `const` item
    static B;
    //~^ ERROR associated `static` items are not allowed
    //~| ERROR missing type for `static` item
}

fn main() {}


