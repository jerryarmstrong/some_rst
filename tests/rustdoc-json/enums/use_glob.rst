tests/rustdoc-json/enums/use_glob.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for <https://github.com/rust-lang/rust/issues/104942>

#![feature(no_core)]
#![no_core]

// @set Color = "$.index[*][?(@.name == 'Color')].id"
pub enum Color {
    Red,
    Green,
    Blue,
}

// @set use_Color = "$.index[*][?(@.kind == 'import')].id"
// @is "$.index[*][?(@.kind == 'import')].inner.id" $Color
// @is "$.index[*][?(@.kind == 'import')].inner.glob" true
pub use Color::*;

// @ismany "$.index[*][?(@.name == 'use_glob')].inner.items[*]" $Color $use_Color


