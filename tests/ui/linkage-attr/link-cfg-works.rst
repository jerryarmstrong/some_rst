tests/ui/linkage-attr/link-cfg-works.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:link-cfg-works-transitive-rlib.rs
// aux-build:link-cfg-works-transitive-dylib.rs

#![feature(link_cfg)]

extern crate link_cfg_works_transitive_dylib;
extern crate link_cfg_works_transitive_rlib;

#[link(name = "foo", cfg(foo))]
extern "C" {}

fn main() {}


