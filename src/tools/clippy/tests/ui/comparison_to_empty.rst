src/tools/clippy/tests/ui/comparison_to_empty.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::comparison_to_empty)]

fn main() {
    // Disallow comparisons to empty
    let s = String::new();
    let _ = s == "";
    let _ = s != "";

    let v = vec![0];
    let _ = v == [];
    let _ = v != [];

    // Allow comparisons to non-empty
    let s = String::new();
    let _ = s == " ";
    let _ = s != " ";

    let v = vec![0];
    let _ = v == [0];
    let _ = v != [0];
}


