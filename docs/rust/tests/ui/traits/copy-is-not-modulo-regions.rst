tests/ui/traits/copy-is-not-modulo-regions.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: not_static yes_static
//[yes_static] check-pass

#[derive(Clone)]
struct Foo<'lt>(&'lt ());

impl Copy for Foo<'static> {}

#[derive(Clone)]
struct Bar<'lt>(Foo<'lt>);

#[cfg(not_static)]
impl<'any> Copy for Bar<'any> {}
//[not_static]~^ the trait `Copy` may not be implemented for this type

#[cfg(yes_static)]
impl<'any> Copy for Bar<'static> {}

fn main() {}


