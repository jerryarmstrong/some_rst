tests/ui/rfc-2632-const-trait-impl/inherent-impl.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]
#![allow(bare_trait_objects)]

struct S;
trait T {}

impl const S {}
//~^ ERROR inherent impls cannot be `const`

impl const T {}
//~^ ERROR inherent impls cannot be `const`

fn main() {}


