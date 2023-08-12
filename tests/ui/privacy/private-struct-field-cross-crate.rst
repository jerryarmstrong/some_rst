tests/ui/privacy/private-struct-field-cross-crate.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:cci_class.rs
extern crate cci_class;
use cci_class::kitties::cat;

fn main() {
  let nyan : cat = cat(52, 99);
  assert_eq!(nyan.meows, 52);
  //~^ ERROR field `meows` of struct `cat` is private
}


