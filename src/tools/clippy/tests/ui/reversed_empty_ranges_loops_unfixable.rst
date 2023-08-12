src/tools/clippy/tests/ui/reversed_empty_ranges_loops_unfixable.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::reversed_empty_ranges)]
#![allow(clippy::uninlined_format_args)]

fn main() {
    for i in 5..5 {
        println!("{}", i);
    }

    for i in (5 + 2)..(8 - 1) {
        println!("{}", i);
    }
}


