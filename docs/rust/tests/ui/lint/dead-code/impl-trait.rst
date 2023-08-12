tests/ui/lint/dead-code/impl-trait.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(dead_code)]

trait Trait {
    type Type;
}

impl Trait for () {
    type Type = ();
}

type Used = ();
type Unused = (); //~ ERROR type alias `Unused` is never used

fn foo() -> impl Trait<Type = Used> {}

fn main() {
    foo();
}


