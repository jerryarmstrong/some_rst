tests/ui/macros/macro-use-bad-args-2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]

#[macro_use(foo="bar")]  //~ ERROR bad macro import
extern crate std;

fn main() {}


