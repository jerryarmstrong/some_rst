tests/ui/unit.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_assignments)]
#![allow(unknown_lints)]
// pretty-expanded FIXME #23616

#![allow(unused_variables)]
#![allow(dead_assignment)]

fn f(u: ()) { return u; }

pub fn main() {
    let u1: () = ();
    let mut u2: () = f(u1);
    u2 = ();
    return ();
}


