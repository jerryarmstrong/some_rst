tests/ui/lint/issue-17718-const-naming.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(unused)]
#![deny(warnings)]

const foo: isize = 3;
//~^ ERROR: should have an upper case name
//~^^ ERROR: constant `foo` is never used

fn main() {}


