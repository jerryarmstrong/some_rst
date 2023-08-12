tests/run-make-fulldeps/crate-hash-rustc-version/b.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate a;

use a::foo;

fn main() {
    let x = String::from("Hello");
    println!("{}", foo(x));
}


