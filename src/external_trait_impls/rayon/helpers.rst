src/external_trait_impls/rayon/helpers.rs
=========================================

Last edited: 2021-03-03 19:20:09

Contents:

.. code-block:: rs

    use alloc::collections::LinkedList;
use alloc::vec::Vec;

use rayon::iter::{IntoParallelIterator, ParallelIterator};

/// Helper for collecting parallel iterators to an intermediary
pub(super) fn collect<I: IntoParallelIterator>(iter: I) -> (LinkedList<Vec<I::Item>>, usize) {
    let list = iter
        .into_par_iter()
        .fold(Vec::new, |mut vec, elem| {
            vec.push(elem);
            vec
        })
        .map(|vec| {
            let mut list = LinkedList::new();
            list.push_back(vec);
            list
        })
        .reduce(LinkedList::new, |mut list1, mut list2| {
            list1.append(&mut list2);
            list1
        });

    let len = list.iter().map(Vec::len).sum();
    (list, len)
}


