tests/ui/traits/anon_trait_static_method_exe.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

// aux-build:anon_trait_static_method_lib.rs

extern crate anon_trait_static_method_lib;
use anon_trait_static_method_lib::Foo;

pub fn main() {
    let x = Foo::new();
    println!("{}", x.x);
}


