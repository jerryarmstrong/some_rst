tests/ui/btreemap/btreemap_into_iterator_lifetime.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std::collections::{BTreeMap, HashMap};

trait Map
where
    for<'a> &'a Self: IntoIterator<Item = (&'a Self::Key, &'a Self::Value)>,
{
    type Key;
    type Value;
}

impl<K, V> Map for HashMap<K, V> {
    type Key = K;
    type Value = V;
}

impl<K, V> Map for BTreeMap<K, V> {
  type Key = K;
  type Value = V;
}

fn main() {}


