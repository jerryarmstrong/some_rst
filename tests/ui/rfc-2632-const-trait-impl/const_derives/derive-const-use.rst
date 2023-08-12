tests/ui/rfc-2632-const-trait-impl/const_derives/derive-const-use.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl, const_cmp, const_default_impls, derive_const)]

pub struct A;

impl const Default for A {
    fn default() -> A { A }
}

impl const PartialEq for A {
    fn eq(&self, _: &A) -> bool { true }
}

#[derive_const(Default, PartialEq)]
pub struct S((), A);

const _: () = assert!(S((), A) == S::default());

fn main() {}


