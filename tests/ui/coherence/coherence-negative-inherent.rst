tests/ui/coherence/coherence-negative-inherent.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(rustc_attrs)]
#![feature(with_negative_coherence)]

#[rustc_strict_coherence]
trait Foo {}

impl !Foo for u32 {}

struct MyStruct<T>(T);

impl<T: Foo> MyStruct<T> {
    fn method(&self) {}
}

impl MyStruct<u32> {
    fn method(&self) {}
}

fn main() {}


