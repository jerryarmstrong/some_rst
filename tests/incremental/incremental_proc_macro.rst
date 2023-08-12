tests/incremental/incremental_proc_macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:incremental_proc_macro_aux.rs
// revisions: cfail1 cfail2
// build-pass (FIXME(62277): could be check-pass?)

// This test makes sure that we still find the proc-macro registrar function
// when we compile proc-macros incrementally (see #47292).

#![crate_type = "rlib"]

#[macro_use]
extern crate incremental_proc_macro_aux;

#[derive(IncrementalMacro)]
pub struct Foo {
    x: u32
}


