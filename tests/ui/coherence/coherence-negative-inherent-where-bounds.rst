tests/ui/coherence/coherence-negative-inherent-where-bounds.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(rustc_attrs)]
#![feature(with_negative_coherence)]

trait Foo {}

impl !Foo for u32 {}

#[rustc_strict_coherence]
struct MyStruct<T>(T);

impl MyStruct<u32> {
    fn method(&self) {}
}

impl<T> MyStruct<T>
where
    T: Foo,
{
    fn method(&self) {}
}

fn main() {}


