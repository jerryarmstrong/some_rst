tests/ui/invalid/invalid-inline.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

#[inline(please,no)] //~ ERROR expected one argument
fn a() {
}

#[inline()] //~ ERROR expected one argument
fn b() {
}

fn main() {
    a();
    b();
}


