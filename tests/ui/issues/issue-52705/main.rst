tests/ui/issues/issue-52705/main.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:png2.rs
// compile-flags:--extern png2
// edition:2018

mod png {
    use png2 as png_ext;

    fn foo() -> png_ext::DecodingError { unimplemented!() }
}

fn main() {
    println!("Hello, world!");
}


