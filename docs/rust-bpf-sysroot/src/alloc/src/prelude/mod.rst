src/alloc/src/prelude/mod.rs
============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    //! The alloc Prelude
//!
//! The purpose of this module is to alleviate imports of commonly-used
//! items of the `alloc` crate by adding a glob import to the top of modules:
//!
//! ```
//! # #![allow(unused_imports)]
//! #![feature(alloc_prelude)]
//! extern crate alloc;
//! use alloc::prelude::v1::*;
//! ```

#![unstable(feature = "alloc_prelude", issue = "58935")]

pub mod v1;


