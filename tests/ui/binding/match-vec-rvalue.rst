tests/ui/binding/match-vec-rvalue.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests that matching rvalues with drops does not crash.



pub fn main() {
    match vec![1, 2, 3] {
        x => {
            assert_eq!(x.len(), 3);
            assert_eq!(x[0], 1);
            assert_eq!(x[1], 2);
            assert_eq!(x[2], 3);
        }
    }
}


