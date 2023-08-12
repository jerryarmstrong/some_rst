src/tools/clippy/tests/ui/flat_map_option.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::flat_map_option)]
#![allow(clippy::redundant_closure, clippy::unnecessary_filter_map)]

fn main() {
    // yay
    let c = |x| Some(x);
    let _ = [1].iter().flat_map(c);
    let _ = [1].iter().flat_map(Some);

    // nay
    let _ = [1].iter().flat_map(|_| &Some(1));
}


