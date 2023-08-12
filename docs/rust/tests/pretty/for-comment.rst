tests/pretty/for-comment.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// pp-exact

fn f(v: &[isize]) -> isize {
    let mut n = 0;
    for e in v {
        n = *e; // This comment once triggered pretty printer bug
    }
    n
}


