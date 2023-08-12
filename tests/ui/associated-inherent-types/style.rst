tests/ui/associated-inherent-types/style.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(inherent_associated_types)]
#![allow(incomplete_features, dead_code)]
#![deny(non_camel_case_types)]

struct S;

impl S {
    type typ = ();
    //~^ ERROR associated type `typ` should have an upper camel case name
}

fn main() {}


