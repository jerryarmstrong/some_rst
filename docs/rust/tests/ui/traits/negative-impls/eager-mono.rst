tests/ui/traits/negative-impls/eager-mono.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags:-C link-dead-code=y

#![feature(negative_impls)]

trait Foo {
    fn foo() {}
}

impl !Foo for () {}

fn main() {}


