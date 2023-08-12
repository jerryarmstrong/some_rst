tests/ui/lazy-type-alias-impl-trait/branches.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl std::fmt::Debug;

fn foo(b: bool) -> Foo {
    if b {
        vec![42_i32]
    } else {
        std::iter::empty().collect()
    }
}

type Bar = impl std::fmt::Debug;

fn bar(b: bool) -> Bar {
    let x: Bar = if b {
        vec![42_i32]
    } else {
        std::iter::empty().collect()
        //~^ ERROR  a value of type `Bar` cannot be built from an iterator over elements of type `_`
    };
    x
}

fn main() {}


