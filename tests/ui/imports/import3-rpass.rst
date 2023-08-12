tests/ui/imports/import3-rpass.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]

use baz::zed;
use baz::zed::bar;

mod baz {
    pub mod zed {
        pub fn bar() { println!("bar2"); }
    }
}

pub fn main() { bar(); }


