tests/ui/use.rs
===============

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(stable_features)]
// pretty-expanded FIXME #23616

#![allow(unused_imports)]
#![feature(start, no_core, core)]
#![no_core]

extern crate std;
extern crate std as zed;

use std::str;
use zed::str as x;

use std::io::{self, Error as IoError, Result as IoResult};
use std::error::{self as foo};
mod baz {
    pub use std::str as x;
}

#[start]
pub fn start(_: isize, _: *const *const u8) -> isize { 0 }


