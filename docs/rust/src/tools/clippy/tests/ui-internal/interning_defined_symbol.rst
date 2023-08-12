src/tools/clippy/tests/ui-internal/interning_defined_symbol.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![deny(clippy::internal)]
#![allow(clippy::missing_clippy_version_attribute, clippy::let_unit_value)]
#![feature(rustc_private)]

extern crate rustc_span;

use rustc_span::symbol::Symbol;

macro_rules! sym {
    ($tt:tt) => {
        rustc_span::symbol::Symbol::intern(stringify!($tt))
    };
}

fn main() {
    // Direct use of Symbol::intern
    let _ = Symbol::intern("f32");

    // Using a sym macro
    let _ = sym!(f32);

    // Correct suggestion when symbol isn't stringified constant name
    let _ = Symbol::intern("proc-macro");

    // interning a keyword
    let _ = Symbol::intern("self");

    // Interning a symbol that is not defined
    let _ = Symbol::intern("xyz123");
    let _ = sym!(xyz123);

    // Using a different `intern` function
    let _ = intern("f32");
}

fn intern(_: &str) {}


