tests/ui/marker_trait_attr/marker-attribute-on-non-trait.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(marker_trait_attr)]

#[marker] //~ ERROR attribute should be applied to a trait
struct Struct {}

#[marker] //~ ERROR attribute should be applied to a trait
impl Struct {}

#[marker] //~ ERROR attribute should be applied to a trait
union Union {
    x: i32,
}

#[marker] //~ ERROR attribute should be applied to a trait
const CONST: usize = 10;

#[marker] //~ ERROR attribute should be applied to a trait
fn function() {}

#[marker] //~ ERROR attribute should be applied to a trait
type Type = ();

fn main() {}


