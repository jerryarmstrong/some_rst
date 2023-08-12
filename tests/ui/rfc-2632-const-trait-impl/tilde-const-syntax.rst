tests/ui/rfc-2632-const-trait-impl/tilde-const-syntax.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z parse-only
// check-pass

#![feature(const_trait_impl)]

struct S<
    T: ~const ?for<'a> Tr<'a> + 'static + ~const std::ops::Add,
    T: ~const ?for<'a: 'b> m::Trait<'a>,
>;


