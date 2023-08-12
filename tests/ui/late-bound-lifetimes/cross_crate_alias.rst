tests/ui/late-bound-lifetimes/cross_crate_alias.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:upstream_alias.rs
// check-pass

extern crate upstream_alias;

fn foo<'a, T: for<'b> upstream_alias::Trait<'b>>(_: upstream_alias::Alias<'a, T>) -> &'a () {
    todo!()
}

fn main() {}


