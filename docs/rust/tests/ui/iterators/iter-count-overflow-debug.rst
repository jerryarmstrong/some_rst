tests/ui/iterators/iter-count-overflow-debug.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// only-32bit too impatient for 2⁶⁴ items
// needs-unwind
// compile-flags: -C debug_assertions=yes -C opt-level=3

use std::panic;

fn main() {
    assert_eq!((0..usize::MAX).by_ref().count(), usize::MAX);

    let r = panic::catch_unwind(|| {
        (0..=usize::MAX).by_ref().count()
    });
    assert!(r.is_err());
}


