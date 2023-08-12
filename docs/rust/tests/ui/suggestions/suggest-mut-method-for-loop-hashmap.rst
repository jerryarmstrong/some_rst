tests/ui/suggestions/suggest-mut-method-for-loop-hashmap.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// https://github.com/rust-lang/rust/issues/82081

use std::collections::HashMap;

struct Test {
    v: u32,
}

fn main() {
    let mut map = HashMap::new();
    map.insert("a", Test { v: 0 });

    for (_k, mut v) in map.iter() {
        //~^ HELP use mutable method
        //~| NOTE this iterator yields `&` references
        v.v += 1;
        //~^ ERROR cannot assign to `v.v`
        //~| NOTE `v` is a `&` reference
    }
}


