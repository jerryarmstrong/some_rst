tests/ui/iterators/array-of-ranges.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    for _ in [0..1] {}
    for _ in [0..=1] {}
    for _ in [0..] {}
    for _ in [..1] {}
    for _ in [..=1] {}
    let start = 0;
    let end = 0;
    for _ in [start..end] {}
    let array_of_range = [start..end];
    for _ in array_of_range {}
    for _ in [0..1, 2..3] {}
    for _ in [0..=1] {}
}


