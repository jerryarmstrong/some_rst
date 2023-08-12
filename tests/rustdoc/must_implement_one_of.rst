tests/rustdoc/must_implement_one_of.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "c"]
#![feature(rustc_attrs)]

#[rustc_must_implement_one_of(a, b)]
// @matches c/trait.Trait.html '//*[@class="stab must_implement"]' \
//      'At least one of the `a`, `b` methods is required.$'
pub trait Trait {
    fn a() {}
    fn b() {}
}


