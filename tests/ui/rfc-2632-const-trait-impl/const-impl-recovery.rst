tests/ui/rfc-2632-const-trait-impl/const-impl-recovery.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait Foo {}

const impl Foo for i32 {} //~ ERROR: expected identifier, found keyword

#[const_trait]
trait Bar {}

const impl<T: Foo> Bar for T {} //~ ERROR: expected identifier, found keyword

const fn still_implements<T: Bar>() {}

const _: () = still_implements::<i32>();

fn main() {}


