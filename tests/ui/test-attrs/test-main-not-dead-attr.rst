tests/ui/test-attrs/test-main-not-dead-attr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test

#![feature(rustc_attrs)]

#![deny(dead_code)]

#[rustc_main]
fn foo() { panic!(); }


