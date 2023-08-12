src/alloc/tests/btree_set_hash.rs
=================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use std::collections::BTreeSet;

#[test]
fn test_hash() {
    use crate::hash;

    let mut x = BTreeSet::new();
    let mut y = BTreeSet::new();

    x.insert(1);
    x.insert(2);
    x.insert(3);

    y.insert(3);
    y.insert(2);
    y.insert(1);

    assert_eq!(hash(&x), hash(&y));
}


