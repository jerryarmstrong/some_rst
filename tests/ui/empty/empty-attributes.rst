tests/ui/empty/empty-attributes.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(lint_reasons)]

#![deny(unused_attributes)]
#![allow()] //~ ERROR unused attribute
#![expect()] //~ ERROR unused attribute
#![warn()] //~ ERROR unused attribute
#![deny()] //~ ERROR unused attribute
#![forbid()] //~ ERROR unused attribute
#![feature()] //~ ERROR unused attribute

#[repr()] //~ ERROR unused attribute
pub struct S;

#[target_feature()] //~ ERROR unused attribute
pub unsafe fn foo() {}

fn main() {}


