tests/ui/dyn-keyword/issue-56327-dyn-trait-in-macro-is-okay.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2015
//
// rust-lang/rust#56327: Some occurrences of `dyn` within a macro are
// not instances of identifiers, and thus should *not* be caught by the
// keyword_ident lint.
//
// Otherwise, rustfix replaces the type `Box<dyn Drop>` with
// `Box<r#dyn Drop>`, which is injecting a bug rather than fixing
// anything.

#![deny(rust_2018_compatibility)]
#![allow(dyn_drop)]

macro_rules! foo {
    () => {
        fn generated_foo() {
            let _x: Box<dyn Drop>;
        }
    }
}

foo!();

fn main() {
    generated_foo();
}


