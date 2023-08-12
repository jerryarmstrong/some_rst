tests/ui/for-loop-while/while-cont.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #825: Should recheck the loop condition after continuing
pub fn main() {
    let mut i = 1;
    while i > 0 {
        assert!((i > 0));
        println!("{}", i);
        i -= 1;
        continue;
    }
}


