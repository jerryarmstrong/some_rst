tests/ui/macros/out-of-order-shadowing.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:define-macro.rs

macro_rules! bar { () => {} }
define_macro!(bar);
bar!(); //~ ERROR `bar` is ambiguous

macro_rules! m { () => { #[macro_use] extern crate define_macro; } }
m!();

fn main() {}


