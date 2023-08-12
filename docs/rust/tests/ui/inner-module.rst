tests/ui/inner-module.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod inner {
    pub mod inner2 {
        pub fn hello() { println!("hello, modular world"); }
    }
    pub fn hello() { inner2::hello(); }
}

pub fn main() { inner::hello(); inner::inner2::hello(); }


