tests/ui/stability-attribute/stability-attribute-implies-no-feature.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:stability-attribute-implies.rs

// Tests that despite the `foobar` feature being implied by now-stable feature `foo`, if `foobar`
// isn't allowed in this crate then an error will be emitted.

extern crate stability_attribute_implies;
use stability_attribute_implies::{foo, foobar};
//~^ ERROR use of unstable library feature 'foobar'

fn main() {
    foo(); // no error - stable
    foobar(); //~ ERROR use of unstable library feature 'foobar'
}


