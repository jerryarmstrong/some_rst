tests/ui/zero-sized/zero-sized-binary-heap-push.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
use std::collections::BinaryHeap;
use std::iter::Iterator;

fn main() {
    const N: usize = 8;

    for len in 0..N {
        let mut tester = BinaryHeap::with_capacity(len);
        assert_eq!(tester.len(), 0);
        assert!(tester.capacity() >= len);
        for bit in 0..len {
            tester.push(());
        }
        assert_eq!(tester.len(), len);
        assert_eq!(tester.iter().count(), len);
        tester.clear();
    }
}


