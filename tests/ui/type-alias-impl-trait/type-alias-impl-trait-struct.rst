tests/ui/type-alias-impl-trait/type-alias-impl-trait-struct.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

type Foo = Vec<impl Send>;

fn make_foo() -> Foo {
    vec![true, false]
}

fn main() {}


