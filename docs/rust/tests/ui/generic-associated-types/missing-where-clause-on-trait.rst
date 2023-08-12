tests/ui/generic-associated-types/missing-where-clause-on-trait.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

trait Foo {
    type Assoc<'a, 'b>;
}
impl Foo for () {
    type Assoc<'a, 'b> = () where 'a: 'b;
    //~^ impl has stricter requirements than trait
}

fn main() {}


