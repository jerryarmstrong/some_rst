tests/ui/lint/lint-non-snake-case-modules.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(non_snake_case)]
#![allow(dead_code)]

mod FooBar { //~ ERROR module `FooBar` should have a snake case name
    pub struct S;
}

fn f(_: FooBar::S) { }

fn main() { }


