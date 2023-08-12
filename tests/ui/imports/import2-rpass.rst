tests/ui/imports/import2-rpass.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use zed::bar;

mod zed {
    pub fn bar() { println!("bar"); }
}

pub fn main() { bar(); }


