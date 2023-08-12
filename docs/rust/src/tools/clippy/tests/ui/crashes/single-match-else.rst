src/tools/clippy/tests/ui/crashes/single-match-else.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::single_match_else)]

//! Test for https://github.com/rust-lang/rust-clippy/issues/1588

fn main() {
    let n = match (42, 43) {
        (42, n) => n,
        _ => panic!("typeck error"),
    };
    assert_eq!(n, 43);
}


