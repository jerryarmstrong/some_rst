tests/ui/borrowck/borrowck-trait-lifetime.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]
// This test verifies that casting from the same lifetime on a value
// to the same lifetime on a trait succeeds. See issue #10766.

// pretty-expanded FIXME #23616

#![allow(dead_code)]

use std::marker;

fn main() {
    trait T { fn foo(&self) {} }

    fn f<'a, V: T>(v: &'a V) -> &'a dyn T {
        v as &'a dyn T
    }
}


