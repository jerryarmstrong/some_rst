tests/ui/type-alias-impl-trait/type-alias-impl-trait-assoc-impl-trait.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

type Foo = impl Iterator<Item = impl Send>;

fn make_foo() -> Foo {
    vec![1, 2].into_iter()
}

type Bar = impl Send;
type Baz = impl Iterator<Item = Bar>;

fn make_baz() -> Baz {
    vec!["1", "2"].into_iter()
}

fn main() {}


