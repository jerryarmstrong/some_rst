tests/ui/traits/default-method/mut.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_assignments)]
// pretty-expanded FIXME #23616

#![allow(unused_variables)]

trait Foo {
    fn foo(&self, mut v: isize) { v = 1; }
}

pub fn main() {}


