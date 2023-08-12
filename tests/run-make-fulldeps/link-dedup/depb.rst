tests/run-make-fulldeps/link-dedup/depb.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(link_cfg)]
#![crate_type = "rlib"]

#[link(name = "testb", cfg(foo))]
extern "C" {}

#[link(name = "testb", cfg(bar))]
extern "C" {}


