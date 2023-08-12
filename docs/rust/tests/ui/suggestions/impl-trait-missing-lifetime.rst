tests/ui/suggestions/impl-trait-missing-lifetime.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(anonymous_lifetime_in_impl_trait)]

// This is understood as `fn foo<'_1>(_: impl Iterator<Item = &'_1 ()>) {}`.
fn f(_: impl Iterator<Item = &'_ ()>) {}

// But that lifetime does not participate in resolution.
fn g(mut x: impl Iterator<Item = &'_ ()>) -> Option<&'_ ()> { x.next() }
//~^ ERROR missing lifetime specifier

// This is understood as `fn foo<'_1>(_: impl Iterator<Item = &'_1 ()>) {}`.
async fn h(_: impl Iterator<Item = &'_ ()>) {}

// But that lifetime does not participate in resolution.
async fn i(mut x: impl Iterator<Item = &'_ ()>) -> Option<&'_ ()> { x.next() }
//~^ ERROR missing lifetime specifier
//~| ERROR lifetime may not live long enough

fn main() {}


