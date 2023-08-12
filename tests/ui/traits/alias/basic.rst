tests/ui/traits/alias/basic.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(trait_alias)]

pub trait Foo {}
pub trait FooAlias = Foo;

fn main() {}


