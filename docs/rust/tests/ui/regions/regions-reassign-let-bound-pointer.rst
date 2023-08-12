tests/ui/regions/regions-reassign-let-bound-pointer.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_assignments)]
#![allow(unused_variables)]
// Check that the type checker permits us to reassign `z` which
// started out with a longer lifetime and was reassigned to a shorter
// one (it should infer to be the intersection).

// pretty-expanded FIXME #23616

fn foo(x: &isize) {
    let a = 1;
    let mut z = x;
    z = &a;
}

pub fn main() {
    foo(&1);
}


