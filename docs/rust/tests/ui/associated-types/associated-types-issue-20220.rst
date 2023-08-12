tests/ui/associated-types/associated-types-issue-20220.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test references to `Self::Item` in the trait. Issue #20220.


use std::vec;

trait IntoIteratorX {
    type Item;
    type IntoIter: Iterator<Item=Self::Item>;

    fn into_iter_x(self) -> Self::IntoIter;
}

impl<T> IntoIteratorX for Vec<T> {
    type Item = T;
    type IntoIter = vec::IntoIter<T>;

    fn into_iter_x(self) -> vec::IntoIter<T> {
        self.into_iter()
    }
}

fn main() {
    let vec = vec![1, 2, 3];
    for (i, e) in vec.into_iter().enumerate() {
        assert_eq!(i+1, e);
    }
}


