library/alloc/tests/btree_set_hash.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::hash;
use std::collections::BTreeSet;

#[test]
fn test_hash() {
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

#[test]
fn test_prefix_free() {
    let x = BTreeSet::from([1, 2, 3]);
    let y = BTreeSet::<i32>::new();

    // If hashed by iteration alone, `(x, y)` and `(y, x)` would visit the same
    // order of elements, resulting in the same hash. But now that we also hash
    // the length, they get distinct sequences of hashed data.
    assert_ne!(hash(&(&x, &y)), hash(&(&y, &x)));
}


