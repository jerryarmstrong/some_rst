tests/ui/rfc-2632-const-trait-impl/tilde_const_on_impl_bound.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl)]

#[const_trait]
trait Foo {
    fn foo(&self) {}
}

struct Bar<T>(T);

impl<T: ~const Foo> Bar<T> {
    const fn foo(&self) {
        self.0.foo()
    }
}

fn main() {}


