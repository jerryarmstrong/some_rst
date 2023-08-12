tests/ui/mismatched_types/issue-38371-unfixable.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn ugh(&[bar]: &u32) {} //~ ERROR expected an array or slice

fn bgh(&&bar: u32) {} //~ ERROR mismatched types

fn main() {}


