tests/ui/specialization/specialization-polarity.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure specialization cannot change impl polarity

#![feature(auto_traits)]
#![feature(negative_impls)]
#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

auto trait Foo {}

impl<T> Foo for T {}
impl !Foo for u8 {} //~ ERROR E0751

auto trait Bar {}

impl<T> !Bar for T {}
impl Bar for u8 {} //~ ERROR E0751

fn main() {}


