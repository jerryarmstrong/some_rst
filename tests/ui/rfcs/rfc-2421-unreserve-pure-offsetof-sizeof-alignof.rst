tests/ui/rfcs/rfc-2421-unreserve-pure-offsetof-sizeof-alignof.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// Test that removed keywords are allowed as identifiers.
fn main () {
    let offsetof = ();
    let alignof = ();
    let sizeof = ();
    let pure = ();
}

fn offsetof() {}
fn alignof() {}
fn sizeof() {}
fn pure() {}


