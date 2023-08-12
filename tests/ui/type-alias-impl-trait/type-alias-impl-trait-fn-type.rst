tests/ui/type-alias-impl-trait/type-alias-impl-trait-fn-type.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
#![allow(dead_code)]

// FIXME: this is ruled out for now but should work

type Foo = fn() -> impl Send;
//~^ ERROR: `impl Trait` only allowed in function and inherent method return types

fn make_foo() -> Foo {
    || 15
}

fn main() {}


