src/tools/clippy/tests/ui/filter_map_identity.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused_imports, clippy::needless_return)]
#![warn(clippy::filter_map_identity)]

fn main() {
    let iterator = vec![Some(1), None, Some(2)].into_iter();
    let _ = iterator.filter_map(|x| x);

    let iterator = vec![Some(1), None, Some(2)].into_iter();
    let _ = iterator.filter_map(std::convert::identity);

    use std::convert::identity;
    let iterator = vec![Some(1), None, Some(2)].into_iter();
    let _ = iterator.filter_map(identity);

    let iterator = vec![Some(1), None, Some(2)].into_iter();
    let _ = iterator.filter_map(|x| return x);
}


