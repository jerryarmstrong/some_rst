tests/ui/lint/inline-trait-and-foreign-items.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]
#![feature(type_alias_impl_trait)]

#![warn(unused_attributes)]

trait Trait {
    #[inline] //~ WARN `#[inline]` is ignored on constants
    //~^ WARN this was previously accepted
    const X: u32;

    #[inline] //~ ERROR attribute should be applied to function or closure
    type T;

    type U;
}

impl Trait for () {
    #[inline] //~ WARN `#[inline]` is ignored on constants
    //~^ WARN this was previously accepted
    const X: u32 = 0;

    #[inline] //~ ERROR attribute should be applied to function or closure
    type T = Self;

    #[inline] //~ ERROR attribute should be applied to function or closure
    type U = impl Trait; //~ ERROR unconstrained opaque type
}

extern "C" {
    #[inline] //~ ERROR attribute should be applied to function or closure
    static X: u32;

    #[inline] //~ ERROR attribute should be applied to function or closure
    type T;
}

fn main() {}


