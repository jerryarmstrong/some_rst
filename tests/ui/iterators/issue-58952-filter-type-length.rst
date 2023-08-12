tests/ui/iterators/issue-58952-filter-type-length.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
//! This snippet causes the type length to blowup exponentially,
//! so check that we don't accidentally exceed the type length limit.
// FIXME: Once the size of iterator adaptors is further reduced,
// increase the complexity of this test.
use std::collections::VecDeque;

fn main() {
    let c = 2;
    let bv = vec![2];
    let b = bv
        .iter()
        .filter(|a| **a == c);

    let _a = vec![1, 2, 3]
        .into_iter()
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .filter(|a| b.clone().any(|b| *b == *a))
        .collect::<VecDeque<_>>();
}


