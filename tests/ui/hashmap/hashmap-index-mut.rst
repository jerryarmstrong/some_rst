tests/ui/hashmap/hashmap-index-mut.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::collections::HashMap;

fn main() {
    let mut map = HashMap::<u32, u32>::new();
    map[&0] = 1; //~ ERROR cannot assign
}


