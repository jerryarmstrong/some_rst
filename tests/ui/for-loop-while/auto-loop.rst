tests/ui/for-loop-while/auto-loop.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let mut sum = 0;
    let xs = vec![1, 2, 3, 4, 5];
    for x in &xs {
        sum += *x;
    }
    assert_eq!(sum, 15);
}


