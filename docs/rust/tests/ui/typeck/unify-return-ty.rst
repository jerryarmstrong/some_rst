tests/ui/typeck/unify-return-ty.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests that the tail expr in null() has its type
// unified with the type *T, and so the type variable
// in that type gets resolved.

// pretty-expanded FIXME #23616

use std::mem;

fn null<T>() -> *const T {
    unsafe {
        mem::transmute(0_usize)
    }
}

pub fn main() { null::<isize>(); }


