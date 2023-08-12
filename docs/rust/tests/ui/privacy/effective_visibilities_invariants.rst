tests/ui/privacy/effective_visibilities_invariants.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Invariant checking doesn't ICE in some cases with errors (issue #104249).

#![feature(staged_api)] //~ ERROR module has missing stability attribute

pub mod m {} //~ ERROR module has missing stability attribute

pub mod m { //~ ERROR the name `m` is defined multiple times
    mod inner {}
    type Inner = u8;
}

fn main() {}


