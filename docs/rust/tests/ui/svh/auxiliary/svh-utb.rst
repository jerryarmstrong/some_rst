tests/ui/svh/auxiliary/svh-utb.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! "svh-uta-trait.rs" is checking that we detect a
//! change from `use foo::TraitB` to use `foo::TraitB` in the hash
//! (SVH) computation (#14132), since that will affect method
//! resolution.
//!
//! This is the downstream crate.

#![crate_name = "utb"]

extern crate uta;

pub fn foo() { assert_eq!(uta::foo::<()>(0), 3); }


