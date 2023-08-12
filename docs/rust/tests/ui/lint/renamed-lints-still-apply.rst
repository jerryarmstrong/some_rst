tests/ui/lint/renamed-lints-still-apply.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type lib
#![deny(single_use_lifetime)]
//~^ WARNING renamed
//~| NOTE `#[warn(renamed_and_removed_lints)]` on by default
//~| NOTE defined here
fn _foo<'a>(_x: &'a u32) {}
//~^ ERROR only used once
//~| NOTE this lifetime
//~| NOTE is used only here


