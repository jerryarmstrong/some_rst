tests/ui/trivial-bounds/trivial-bounds-leak-copy.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that false Copy bounds don't leak
#![feature(trivial_bounds)]

fn copy_out_string(t: &String) -> String where String: Copy {
    *t
}

fn move_out_string(t: &String) -> String {
    *t //~ ERROR
}

fn main() {}


