src/tools/clippy/tests/ui/entry_btree.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::map_entry)]
#![allow(dead_code)]

use std::collections::BTreeMap;

fn foo() {}

fn btree_map<K: Eq + Ord + Copy, V: Copy>(m: &mut BTreeMap<K, V>, k: K, v: V) {
    // insert then do something, use if let
    if !m.contains_key(&k) {
        m.insert(k, v);
        foo();
    }
}

fn main() {}


