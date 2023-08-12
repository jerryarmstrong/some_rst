tests/ui/symbol-names/impl2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![feature(rustc_attrs)]
#![allow(dead_code)]

trait Foo {
    fn baz();
}

impl Foo for [u8; 1 + 2] {
    #[rustc_def_path] //~ ERROR def-path(<[u8; 1 + 2] as Foo>::baz)
    fn baz() {}
}

fn main() {}


