tests/ui/imports/import-prefix-macro-1.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub mod b {
        pub mod c {
            pub struct S;
            pub struct Z;
        }
    }
}

macro_rules! import {
    ($p: path) => (use $p {S, Z}); //~ERROR expected one of `::`, `;`, or `as`, found `{`
}

import! { a::b::c }

fn main() {}


