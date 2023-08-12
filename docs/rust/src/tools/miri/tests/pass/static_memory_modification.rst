src/tools/miri/tests/pass/static_memory_modification.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::sync::atomic::{AtomicUsize, Ordering};

static mut X: usize = 5;
static Y: AtomicUsize = AtomicUsize::new(5);

fn main() {
    unsafe {
        X = 6;
        assert_eq!(X, 6);
    }

    Y.store(6, Ordering::Relaxed);
    assert_eq!(Y.load(Ordering::Relaxed), 6);
}


