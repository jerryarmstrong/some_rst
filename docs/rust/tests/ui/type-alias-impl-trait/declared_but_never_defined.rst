tests/ui/type-alias-impl-trait/declared_but_never_defined.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

// declared but never defined
type Bar = impl std::fmt::Debug; //~ ERROR unconstrained opaque type


