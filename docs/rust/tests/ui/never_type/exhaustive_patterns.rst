tests/ui/never_type/exhaustive_patterns.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// known-bug: #104034

#![feature(exhaustive_patterns, never_type)]

mod inner {
    pub struct Wrapper<T>(T);
}

enum Either<A, B> {
    A(A),
    B(inner::Wrapper<B>),
}

fn foo() -> Either<(), !> {
    Either::A(())
}

fn main() {
    let Either::A(()) = foo();
}


