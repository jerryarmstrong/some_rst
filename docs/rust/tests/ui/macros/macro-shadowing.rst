tests/ui/macros/macro-shadowing.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:two_macros.rs

#![allow(unused_macros)]

macro_rules! foo { () => {} }
macro_rules! macro_one { () => {} }
#[macro_use(macro_two)] extern crate two_macros;

macro_rules! m1 { () => {
    macro_rules! foo { () => {} }

    #[macro_use] //~ ERROR `macro_two` is already in scope
    extern crate two_macros as __;
}}
m1!();

foo!(); //~ ERROR `foo` is ambiguous

macro_rules! m2 { () => {
    macro_rules! foo { () => {} }
    foo!();
}}
m2!();
//^ Since `foo` is not used outside this expansion, it is not a shadowing error.

fn main() {}


