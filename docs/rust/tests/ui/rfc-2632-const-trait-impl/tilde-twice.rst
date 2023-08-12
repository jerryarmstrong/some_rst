tests/ui/rfc-2632-const-trait-impl/tilde-twice.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z parse-only

#![feature(const_trait_impl)]

struct S<T: ~const ~const Tr>;
//~^ ERROR expected identifier, found `~`


