tests/ui/rfc-2632-const-trait-impl/trait-where-clause-self-referential.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl)]

#[const_trait]
trait Foo {
    fn bar() where Self: ~const Foo;
}

struct S;

impl Foo for S {
    fn bar() {}
}

fn baz<T: Foo>() {
    T::bar();
}

const fn qux<T: ~const Foo>() {
    T::bar();
}

fn main() {}


