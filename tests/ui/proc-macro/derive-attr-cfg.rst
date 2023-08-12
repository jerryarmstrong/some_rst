tests/ui/proc-macro/derive-attr-cfg.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// aux-build:derive-attr-cfg.rs

extern crate derive_attr_cfg;
use derive_attr_cfg::Foo;

#[derive(Foo)]
#[foo]
struct S {
    #[cfg(any())]
    x: i32
}

fn main() {
}


