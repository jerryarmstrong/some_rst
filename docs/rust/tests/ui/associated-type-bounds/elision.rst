tests/ui/associated-type-bounds/elision.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_type_bounds)]
#![feature(anonymous_lifetime_in_impl_trait)]

// The same thing should happen for constraints in dyn trait.
fn f(x: &mut dyn Iterator<Item: Iterator<Item = &'_ ()>>) -> Option<&'_ ()> { x.next() }
//~^ ERROR missing lifetime specifier
//~| ERROR mismatched types

fn main() {}


