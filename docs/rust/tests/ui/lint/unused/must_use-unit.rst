tests/ui/lint/unused/must_use-unit.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]
#![deny(unused_must_use)]

#[must_use]
fn foo() {}

#[must_use]
fn bar() -> ! {
    unimplemented!()
}

fn main() {
    foo(); //~ unused return value of `foo`

    bar(); //~ unused return value of `bar`
}


