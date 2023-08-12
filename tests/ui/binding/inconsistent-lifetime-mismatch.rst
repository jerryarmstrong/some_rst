tests/ui/binding/inconsistent-lifetime-mismatch.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn foo(_: &[&str]) {}

fn bad(a: &str, b: &str) {
    foo(&[a, b]);
}

fn good(a: &str, b: &str) {
    foo(&[a, b]);
}

fn main() {}


