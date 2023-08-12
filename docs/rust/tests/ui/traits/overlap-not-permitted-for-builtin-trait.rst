tests/ui/traits/overlap-not-permitted-for-builtin-trait.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![feature(negative_impls)]

// Overlapping negative impls for `MyStruct` are not permitted:
struct MyStruct;
impl !Send for MyStruct {}
impl !Send for MyStruct {}
//~^ ERROR conflicting implementations of trait

fn main() {}


