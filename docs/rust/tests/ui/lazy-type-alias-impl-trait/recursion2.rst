tests/ui/lazy-type-alias-impl-trait/recursion2.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

// check-pass

type Foo = impl std::fmt::Debug;

fn foo(b: bool) -> Foo {
    if b {
        return vec![];
    }
    let x: Vec<i32> = foo(false);
    std::iter::empty().collect()
}

fn bar(b: bool) -> impl std::fmt::Debug {
    if b {
        return vec![]
    }
    let x: Vec<i32> = bar(false);
    std::iter::empty().collect()
}

fn main() {}


