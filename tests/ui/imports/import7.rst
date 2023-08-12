tests/ui/imports/import7.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]

use foo::zed;
use bar::baz;

mod foo {
    pub mod zed {
        pub fn baz() { println!("baz"); }
    }
}
mod bar {
    pub use foo::zed::baz;
    pub mod foo {
        pub mod zed {}
    }
}
pub fn main() { baz(); }


