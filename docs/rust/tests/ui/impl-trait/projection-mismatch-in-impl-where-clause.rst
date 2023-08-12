tests/ui/impl-trait/projection-mismatch-in-impl-where-clause.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Super {
    type Assoc;
}

impl Super for () {
    type Assoc = u8;
}

pub trait Test {}

impl<T> Test for T where T: Super<Assoc = ()> {}

fn test() -> impl Test {
    //~^ERROR type mismatch resolving `<() as Super>::Assoc == ()`
    ()
}

fn main() {
    let a = test();
}


