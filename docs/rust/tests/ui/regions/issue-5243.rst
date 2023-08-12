tests/ui/regions/issue-5243.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Check that merely having lifetime parameters is not
// enough for codegen to consider this as non-monomorphic,
// which led to various assertions and failures in turn.

// pretty-expanded FIXME #23616

struct S<'a> {
    v: &'a isize
}

fn f<'lt>(_s: &'lt S<'lt>) {}

pub fn main() {
    f(& S { v: &42 });
}


