src/tools/clippy/tests/ui/pub_use.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::pub_use)]
#![allow(unused_imports)]
#![no_main]

pub mod outer {
    mod inner {
        pub struct Test {}
    }
    // should be linted
    pub use inner::Test;
}

// should not be linted
use std::fmt;


