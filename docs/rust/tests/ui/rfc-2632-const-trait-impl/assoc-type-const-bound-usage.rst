tests/ui/rfc-2632-const-trait-impl/assoc-type-const-bound-usage.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl)]

#[const_trait]
trait Foo {
    type Assoc: ~const Foo;
    fn foo() {}
}

const fn foo<T: ~const Foo>() {
    <T as Foo>::Assoc::foo();
}

fn main() {}


