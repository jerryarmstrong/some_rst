tests/ui/hygiene/trait_items-2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// ignore-pretty pretty-printing is unhygienic

#![feature(decl_macro)]

macro m($T:ident, $f:ident) {
    pub trait $T {
        fn f(&self) -> u32 { 0 }
        fn $f(&self) -> i32 { 0 }
    }
    impl $T for () {}

    let _: u32 = ().f();
    let _: i32 = ().$f();
}

fn main() {
    m!(T, f);
    let _: i32 = ().f();
}


