tests/ui/associated-types/default-associated-types.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(associated_type_defaults)]

trait Foo<T: Default + ToString> {
    type Out: Default + ToString = T;
}

impl Foo<u32> for () {
}

impl Foo<u64> for () {
    type Out = bool;
}

fn main() {
    assert_eq!(
        <() as Foo<u32>>::Out::default().to_string(),
        "0");
    assert_eq!(
        <() as Foo<u64>>::Out::default().to_string(),
        "false");
}


