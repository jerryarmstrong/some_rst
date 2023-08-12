tests/ui/array-slice-vec/new-style-fixed-length-vec.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

static FOO: [isize; 3] = [1, 2, 3];

pub fn main() {
    println!("{} {} {}", FOO[0], FOO[1], FOO[2]);
}


