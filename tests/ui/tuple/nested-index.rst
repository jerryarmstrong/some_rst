tests/ui/tuple/nested-index.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main () {
    let n = (1, (2, 3)).1.1;
    assert_eq!(n, 3);

    let n = (1, (2, (3, 4))).1.1.1;
    assert_eq!(n, 4);

    // This is a range expression, not nested indexing.
    let _ = 0.0..1.1;
}


