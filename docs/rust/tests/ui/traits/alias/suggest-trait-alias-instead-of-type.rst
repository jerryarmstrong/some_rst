tests/ui/traits/alias/suggest-trait-alias-instead-of-type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test of #43913.

// run-rustfix

#![feature(trait_alias)]
#![allow(bare_trait_objects, dead_code)]

type Strings = Iterator<Item=String>;

struct Struct<S: Strings>(S);
//~^ ERROR: expected trait, found type alias `Strings`

fn main() {}


