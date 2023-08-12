tests/ui/proc-macro/unsafe-mod.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:macro-only-syntax.rs

#![feature(proc_macro_hygiene)]

extern crate macro_only_syntax;

#[macro_only_syntax::expect_unsafe_mod]
unsafe mod m {
    pub unsafe mod inner;
}

fn main() {}


