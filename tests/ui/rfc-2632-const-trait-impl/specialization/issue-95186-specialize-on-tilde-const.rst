tests/ui/rfc-2632-const-trait-impl/specialization/issue-95186-specialize-on-tilde-const.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that `~const` trait bounds can be used to specialize const trait impls.

// check-pass

#![feature(const_trait_impl)]
#![feature(rustc_attrs)]
#![feature(min_specialization)]

#[const_trait]
#[rustc_specialization_trait]
trait Specialize {}

#[const_trait]
trait Foo {}

impl<T> const Foo for T {}

impl<T> const Foo for T
where
    T: ~const Specialize,
{}

#[const_trait]
trait Bar {}

impl<T> const Bar for T
where
    T: ~const Foo,
{}

impl<T> const Bar for T
where
    T: ~const Foo,
    T: ~const Specialize,
{}

fn main() {}


