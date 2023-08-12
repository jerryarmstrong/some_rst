src/tools/miri/tests/fail/shims/sync/libc_pthread_rwlock_unlock_unlocked.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

fn main() {
    let rw = std::cell::UnsafeCell::new(libc::PTHREAD_RWLOCK_INITIALIZER);
    unsafe {
        libc::pthread_rwlock_unlock(rw.get()); //~ ERROR: was not locked
    }
}


