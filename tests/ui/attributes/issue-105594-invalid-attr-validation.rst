tests/ui/attributes/issue-105594-invalid-attr-validation.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This checks that the attribute validation ICE in issue #105594 doesn't
// recur.
//
// ignore-thumbv8m.base
#![feature(cmse_nonsecure_entry)]

fn main() {}

#[track_caller] //~ ERROR attribute should be applied to a function
static _A: () = ();

#[cmse_nonsecure_entry] //~ ERROR attribute should be applied to a function
static _B: () = (); //~| ERROR #[cmse_nonsecure_entry]` is only valid for targets


