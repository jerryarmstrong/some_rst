tests/ui/macros/macro-multiple-matcher-bindings.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that duplicate matcher binding names are caught at declaration time, rather than at macro
// invocation time.

#![allow(unused_macros)]

macro_rules! foo1 {
    ($a:ident, $a:ident) => {}; //~ERROR duplicate matcher binding
    ($a:ident, $a:path) => {};  //~ERROR duplicate matcher binding
}

macro_rules! foo2 {
    ($a:ident) => {}; // OK
    ($a:path) => {};  // OK
}

macro_rules! foo3 {
    ($a:ident, $($a:ident),*) => {}; //~ERROR duplicate matcher binding
    ($($a:ident)+ # $($($a:path),+);*) => {}; //~ERROR duplicate matcher binding
}

fn main() {}


