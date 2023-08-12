tests/ui/lint/lint-change-warnings.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(warnings)]
#![allow(dead_code)]

fn main() {
    while true {} //~ ERROR: infinite
}

#[allow(warnings)]
fn foo() {
    while true {}
}

#[warn(warnings)]
fn bar() {
    while true {} //~ WARNING: infinite
}

#[forbid(warnings)]
fn baz() {
    while true {} //~ ERROR: infinite
}


