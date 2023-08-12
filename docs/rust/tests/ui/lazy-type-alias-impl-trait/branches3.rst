tests/ui/lazy-type-alias-impl-trait/branches3.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl for<'a> FnOnce(&'a str) -> usize;
type Bar = impl FnOnce(&'static str) -> usize;

fn foo() -> Foo {
    if true {
        |s| s.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}
fn bar() -> Bar {
    if true {
        |s| s.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}

fn foo2() -> impl for<'a> FnOnce(&'a str) -> usize {
    if true {
        |s| s.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}
fn bar2() -> impl FnOnce(&'static str) -> usize {
    if true {
        |s| s.len() //~ ERROR type annotations needed
    } else {
        panic!()
    }
}

fn main() {}


