tests/ui/lint/lint-non-snake-case-lifetimes.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(non_snake_case)]
#![allow(dead_code)]

fn f<'FooBar>( //~ ERROR lifetime `'FooBar` should have a snake case name
    _: &'FooBar ()
) {}

fn main() { }


