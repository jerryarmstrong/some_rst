tests/ui/return-nil.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn f() { let x: () = (); return x; }

pub fn main() { let _x = f(); }


