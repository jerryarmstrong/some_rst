tests/ui/keyword/keyword-self-as-type-param.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test of #36638.

struct Foo<Self>(Self);
//~^ ERROR unexpected keyword `Self` in generic parameters
//~| ERROR recursive type `Foo` has infinite size

trait Bar<Self> {}
//~^ ERROR unexpected keyword `Self` in generic parameters

fn main() {}


