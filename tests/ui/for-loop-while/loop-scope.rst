tests/ui/for-loop-while/loop-scope.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = vec![10, 20, 30];
    let mut sum = 0;
    for x in &x { sum += *x; }
    assert_eq!(sum, 60);
}


