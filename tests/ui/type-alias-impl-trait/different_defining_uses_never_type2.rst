tests/ui/type-alias-impl-trait/different_defining_uses_never_type2.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![feature(type_alias_impl_trait)]

fn main() {}

// two definitions with different types
type Foo = impl std::fmt::Debug;

fn foo() -> Foo {
    ""
}

fn bar(arg: bool) -> Foo {
    if arg {
        panic!()
    } else {
        "bar"
    }
}

fn boo(arg: bool) -> Foo {
    if arg {
        loop {}
    } else {
        "boo"
    }
}

fn bar2(arg: bool) -> Foo {
    if arg {
        "bar2"
    } else {
        panic!()
    }
}

fn boo2(arg: bool) -> Foo {
    if arg {
        "boo2"
    } else {
        loop {}
    }
}


