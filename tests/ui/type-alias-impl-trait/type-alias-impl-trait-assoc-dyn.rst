tests/ui/type-alias-impl-trait/type-alias-impl-trait-assoc-dyn.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

type Foo = Box<dyn Iterator<Item = impl Send>>;

fn make_foo() -> Foo {
    Box::new(vec![1, 2, 3].into_iter())
}

fn main() {}


