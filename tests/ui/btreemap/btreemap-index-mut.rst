tests/ui/btreemap/btreemap-index-mut.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::collections::BTreeMap;

fn main() {
    let mut map = BTreeMap::<u32, u32>::new();
    map[&0] = 1; //~ ERROR cannot assign
}


