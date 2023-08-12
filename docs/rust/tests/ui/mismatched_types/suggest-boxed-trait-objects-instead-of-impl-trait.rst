tests/ui/mismatched_types/suggest-boxed-trait-objects-instead-of-impl-trait.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(dead_code)]

struct S;
struct Y;

trait Trait {}

impl Trait for S {}
impl Trait for Y {}

fn foo() -> impl Trait {
    if true {
        S
    } else {
        Y //~ ERROR `if` and `else` have incompatible types
    }
}

fn bar() -> impl Trait {
    match true {
        true => S,
        false => Y, //~ ERROR `match` arms have incompatible types
    }
}

fn main() {}


