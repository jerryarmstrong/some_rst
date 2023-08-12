tests/ui/artificial-block.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f() -> isize { { return 3; } }

pub fn main() { assert_eq!(f(), 3); }


