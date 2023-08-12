tests/ui/lang-items/lang-item-missing.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a missing lang item (in this case `sized`) does not cause an ICE,
// see #17392.

// error-pattern: requires `sized` lang_item

#![feature(start, no_core)]
#![no_core]

#[start]
fn start(argc: isize, argv: *const *const u8) -> isize {
    0
}


