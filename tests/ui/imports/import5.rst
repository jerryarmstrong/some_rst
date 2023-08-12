tests/ui/imports/import5.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use foo::bar;
mod foo {
    pub use foo::zed::bar;
    pub mod zed {
        pub fn bar() { println!("foo"); }
    }
}

pub fn main() { bar(); }


