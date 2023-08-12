tests/ui/type-alias-impl-trait/type-alias-impl-trait-with-no-traits.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl 'static;
//~^ ERROR: at least one trait must be specified

fn foo() -> Foo {
    "foo"
}

fn bar() -> impl 'static { //~ ERROR: at least one trait must be specified
    "foo"
}

fn main() {}


