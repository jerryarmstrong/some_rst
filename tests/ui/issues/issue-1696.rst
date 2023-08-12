tests/ui/issues/issue-1696.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::collections::HashMap;

pub fn main() {
    let mut m = HashMap::new();
    m.insert(b"foo".to_vec(), b"bar".to_vec());
    println!("{:?}", m);
}


