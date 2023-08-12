tests/ui/async-await/nested-in-impl.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that async fn works when nested inside of
// impls with lifetime parameters.
//
// check-pass
// edition:2018

struct Foo<'a>(&'a ());

impl<'a> Foo<'a> {
    fn test() {
        async fn test() {}
    }
}

fn main() { }


