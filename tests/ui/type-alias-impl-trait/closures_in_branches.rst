tests/ui/type-alias-impl-trait/closures_in_branches.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl std::ops::FnOnce(String) -> usize;

fn foo(b: bool) -> Foo {
    if b {
        |x| x.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}


type Foo1 = impl std::ops::FnOnce(String) -> usize;
fn foo1(b: bool) -> Foo1 {
    |x| x.len()
}

fn bar(b: bool) -> impl std::ops::FnOnce(String) -> usize {
    if b {
        |x| x.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}

fn bar1(b: bool) -> impl std::ops::FnOnce(String) -> usize {
    |x| x.len()
}

fn main() {}


