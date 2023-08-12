tests/ui/wrong-hashset-issue-42918.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
//
#![allow(dead_code)]
// compile-flags: -O

use std::collections::HashSet;

#[derive(PartialEq, Debug, Hash, Eq, Clone, PartialOrd, Ord)]
enum MyEnum {
    E0,

    E1,

    E2,
    E3,
    E4,

    E5,
    E6,
    E7,
}


fn main() {
    use MyEnum::*;
    let s: HashSet<_> = [E4, E1].iter().cloned().collect();
    let mut v: Vec<_> = s.into_iter().collect();
    v.sort();

    assert_eq!([E1, E4], &v[..]);
}


