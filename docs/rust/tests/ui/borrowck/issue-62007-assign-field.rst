tests/ui/borrowck/issue-62007-assign-field.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Issue #62007: assigning over a field projection (`list.0 = n;` in
// this case) should be able to kill all borrows of `list.0`, so that
// `list.0` can be borrowed on the next iteration through the loop.

#![allow(dead_code)]

struct List<T> {
    value: T,
    next: Option<Box<List<T>>>,
}

fn to_refs<T>(mut list: (&mut List<T>,)) -> Vec<&mut T> {
    let mut result = vec![];
    loop {
        result.push(&mut (list.0).value);
        if let Some(n) = (list.0).next.as_mut() {
            list.0 = n;
        } else {
            return result;
        }
    }
}

fn main() {}


