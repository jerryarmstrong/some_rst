tests/ui/impl-trait/issues/infinite-impl-trait-issue-38064.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that attempts to construct infinite types via impl trait fail
// in a graceful way.
//
// Regression test for #38064.

trait Quux {}

fn foo() -> impl Quux { //~ ERROR cannot resolve opaque type
    struct Foo<T>(T);
    impl<T> Quux for Foo<T> {}
    Foo(bar())
}

fn bar() -> impl Quux { //~ ERROR cannot resolve opaque type
    struct Bar<T>(T);
    impl<T> Quux for Bar<T> {}
    Bar(foo())
}

// effectively:
//     struct Foo(Bar);
//     struct Bar(Foo);
// should produce an error about infinite size

fn main() { foo(); }


