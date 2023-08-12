tests/ui/macros/macro-in-fn.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(decl_macro)]

pub fn moo() {
    pub macro ABC() {{}}
}

fn main() {}


