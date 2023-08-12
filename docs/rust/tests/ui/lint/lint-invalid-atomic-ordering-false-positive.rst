tests/ui/lint/lint-invalid-atomic-ordering-false-positive.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64
// check-pass
use std::sync::atomic::{AtomicUsize, Ordering};

trait Foo {
    fn store(self, ordering: Ordering);
}

impl Foo for AtomicUsize {
    fn store(self, _ordering: Ordering) {
        AtomicUsize::store(&self, 4, Ordering::SeqCst);
    }
}

fn main() {
    let x = AtomicUsize::new(3);
    x.store(Ordering::Acquire);
}


