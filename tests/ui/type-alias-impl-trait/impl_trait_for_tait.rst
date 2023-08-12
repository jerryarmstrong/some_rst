tests/ui/type-alias-impl-trait/impl_trait_for_tait.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib
// check-pass

#![feature(type_alias_impl_trait)]
type Alias = impl Sized;

fn constrain() -> Alias {
    1i32
}

trait HideIt {
    type Assoc;
}

impl HideIt for () {
    type Assoc = Alias;
}

pub trait Yay {}

impl Yay for <() as HideIt>::Assoc {}


