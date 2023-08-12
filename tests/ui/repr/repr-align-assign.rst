tests/ui/repr/repr-align-assign.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(dead_code)]

#[repr(align=8)] //~ ERROR incorrect `repr(align)` attribute format
                 //~| ERROR incorrect `repr(align)` attribute format
struct A(u64);

#[repr(align="8")] //~ ERROR incorrect `repr(align)` attribute format
                   //~| ERROR incorrect `repr(align)` attribute format
struct B(u64);

fn main() {}


