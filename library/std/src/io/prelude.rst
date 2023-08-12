library/std/src/io/prelude.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! The I/O Prelude.
//!
//! The purpose of this module is to alleviate imports of many common I/O traits
//! by adding a glob import to the top of I/O heavy modules:
//!
//! ```
//! # #![allow(unused_imports)]
//! use std::io::prelude::*;
//! ```

#![stable(feature = "rust1", since = "1.0.0")]

#[stable(feature = "rust1", since = "1.0.0")]
pub use super::{BufRead, Read, Seek, Write};


