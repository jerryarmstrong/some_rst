tests/incremental/issue-84252-global-alloc.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail1 cfail2
// build-pass

#![crate_type="lib"]
#![crate_type="cdylib"]

#[allow(unused_imports)]
use std::alloc::System;

#[cfg(cfail1)]
#[global_allocator]
static ALLOC: System = System;


