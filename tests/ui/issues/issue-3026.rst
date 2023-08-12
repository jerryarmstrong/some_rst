tests/ui/issues/issue-3026.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::collections::HashMap;

pub fn main() {
    let x: Box<_>;
    let mut buggy_map: HashMap<usize, &usize> = HashMap::new();
    x = Box::new(1);
    buggy_map.insert(42, &*x);
}


