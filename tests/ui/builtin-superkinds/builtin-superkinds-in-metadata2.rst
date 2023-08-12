tests/ui/builtin-superkinds/builtin-superkinds-in-metadata2.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]

// aux-build:trait_superkinds_in_metadata.rs

// Tests (correct) usage of trait super-builtin-kinds cross-crate.

extern crate trait_superkinds_in_metadata;
use trait_superkinds_in_metadata::{RequiresRequiresShareAndSend, RequiresShare};
use trait_superkinds_in_metadata::RequiresCopy;
use std::marker;

#[derive(Copy, Clone)]
struct X<T>(#[allow(unused_tuple_struct_fields)] T);

impl<T:Sync> RequiresShare for X<T> { }

impl<T:Sync+Send> RequiresRequiresShareAndSend for X<T> { }

impl<T:Copy> RequiresCopy for X<T> { }

pub fn main() { }


