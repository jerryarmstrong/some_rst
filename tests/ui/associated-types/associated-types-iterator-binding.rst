tests/ui/associated-types/associated-types-iterator-binding.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn pairwise_sub<T:DoubleEndedIterator<Item=isize>>(mut t: T) -> isize {
    let mut result = 0;
    loop {
        let front = t.next();
        let back = t.next_back();
        match (front, back) {
            (Some(f), Some(b)) => { result += b - f; }
            _ => { return result; }
        }
    }
}

fn main() {
    let v = vec![1, 2, 3, 4, 5, 6];
    let r = pairwise_sub(v.into_iter());
    assert_eq!(r, 9);
}


