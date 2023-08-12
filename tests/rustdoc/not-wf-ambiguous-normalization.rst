tests/rustdoc/not-wf-ambiguous-normalization.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Znormalize-docs

#![feature(type_alias_impl_trait)]

trait Allocator {
    type Buffer;
}

struct DefaultAllocator;

// This unconstrained impl parameter causes the normalization of
// `<DefaultAllocator as Allocator>::Buffer` to be ambiguous,
// which caused an ICE with `-Znormalize-docs`.
impl<T> Allocator for DefaultAllocator {
    type Buffer = ();
}

type A = impl Fn(<DefaultAllocator as Allocator>::Buffer);

fn foo() -> A {
    |_| ()
}

fn main() {}


