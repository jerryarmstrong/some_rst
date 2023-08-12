src/tools/clippy/tests/ui/crashes/needless_lifetimes_impl_trait.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::needless_lifetimes)]
#![allow(dead_code)]

trait Foo {}

struct Bar;

struct Baz<'a> {
    bar: &'a Bar,
}

impl<'a> Foo for Baz<'a> {}

impl Bar {
    fn baz<'a>(&'a self) -> impl Foo + 'a {
        Baz { bar: self }
    }
}

fn main() {}


