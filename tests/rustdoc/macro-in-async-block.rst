tests/rustdoc/macro-in-async-block.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression issue for rustdoc ICE encountered in PR #72088.
// edition:2018
#![feature(decl_macro)]

fn main() {
    async {
        macro m() {}
    };
}


