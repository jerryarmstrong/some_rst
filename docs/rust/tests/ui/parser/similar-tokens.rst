tests/ui/parser/similar-tokens.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_imports)]

pub mod x {
    pub struct A;
    pub struct B;
}

// `.` is similar to `,` so list parsing should continue to closing `}`
use x::{A. B}; //~ ERROR expected one of `,`, `::`, `as`, or `}`, found `.`

fn main() {}


