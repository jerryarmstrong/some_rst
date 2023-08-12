tests/ui/lazy-type-alias-impl-trait/recursion3.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl std::fmt::Debug;

fn foo(b: bool) -> Foo {
    if b {
        return 42
    }
    let x: u32 = foo(false) + 42; //~ ERROR cannot add
    99
}

fn bar(b: bool) -> impl std::fmt::Debug {
    if b {
        return 42
    }
    let x: u32 = bar(false) + 42; //~ ERROR cannot add
    99
}

fn main() {}


