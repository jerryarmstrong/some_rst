tests/ui/threads-sendsync/std-sync-right-kind-impls.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::sync;

fn assert_both<T: Sync + Send>() {}

fn main() {
    assert_both::<sync::Mutex<()>>();
    assert_both::<sync::Condvar>();
    assert_both::<sync::RwLock<()>>();
    assert_both::<sync::Barrier>();
    assert_both::<sync::Arc<()>>();
    assert_both::<sync::Weak<()>>();
    assert_both::<sync::Once>();
}


