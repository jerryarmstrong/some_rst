tests/ui/type-alias-impl-trait/field-types.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![allow(dead_code)]

// check-pass

use std::fmt::Debug;

type Foo = impl Debug;

struct Bar {
    foo: Foo,
}

fn bar() -> Bar {
    Bar { foo: "foo" }
}

fn main() {}


