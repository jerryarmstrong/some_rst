tests/ui/generic-associated-types/mismatched-where-clause-regions.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type T<'a1, 'b1>
    where
        'a1: 'b1;
}

impl Foo for () {
    type T<'a2, 'b2> = () where 'b2: 'a2;
    //~^ ERROR impl has stricter requirements than trait
}

fn main() {}


