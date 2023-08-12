tests/ui/type-alias-impl-trait/issue-52843-closure-constrain.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks to ensure that we properly detect when a closure constrains an opaque type

#![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {
    type Opaque = impl Debug;
    fn _unused() -> Opaque { String::new() }
    let null = || -> Opaque { 0 };
    //~^ ERROR: concrete type differs from previous defining opaque type use
    println!("{:?}", null());
}


