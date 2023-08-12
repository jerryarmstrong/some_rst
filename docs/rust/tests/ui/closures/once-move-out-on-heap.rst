tests/ui/closures/once-move-out-on-heap.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Testing guarantees provided by once functions.



use std::sync::Arc;

fn foo<F:FnOnce()>(blk: F) {
    blk();
}

pub fn main() {
    let x = Arc::new(true);
    foo(move|| {
        assert!(*x);
        drop(x);
    });
}


