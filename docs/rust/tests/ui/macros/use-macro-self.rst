tests/ui/macros/use-macro-self.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]
// aux-build:use-macro-self.rs

#[macro_use]
extern crate use_macro_self;

use use_macro_self::foobarius::{self};

fn main() {
    let _: () = foobarius!(); // OK, the macro returns `()`
}


