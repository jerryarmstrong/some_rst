tests/ui/once-cant-call-twice-on-heap.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing guarantees provided by once functions.
// This program would segfault if it were legal.

use std::sync::Arc;

fn foo<F:FnOnce()>(blk: F) {
    blk();
    blk(); //~ ERROR use of moved value
}

fn main() {
    let x = Arc::new(true);
    foo(move|| {
        assert!(*x);
        drop(x);
    });
}


