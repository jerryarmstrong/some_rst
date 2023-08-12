tests/ui/lint/lint-non-uppercase-associated-const.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(non_upper_case_globals)]
#![allow(dead_code)]

struct Foo;

impl Foo {
    const not_upper: bool = true;
}
//~^^ ERROR associated constant `not_upper` should have an upper case name

fn main() {}


