tests/ui/type-ptr.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn f(a: *const isize) -> *const isize { return a; }

fn g(a: *const isize) -> *const isize { let b = f(a); return b; }

pub fn main() { return; }


