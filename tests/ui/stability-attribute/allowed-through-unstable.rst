tests/ui/stability-attribute/allowed-through-unstable.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for new `#[rustc_allowed_through_unstable_modules]` attribute
//
// aux-build:allowed-through-unstable-core.rs
#![crate_type = "lib"]

extern crate allowed_through_unstable_core;

use allowed_through_unstable_core::unstable_module::OldStableTraitAllowedThoughUnstable;
use allowed_through_unstable_core::unstable_module::NewStableTraitNotAllowedThroughUnstable; //~ ERROR use of unstable library feature 'unstable_test_feature'


