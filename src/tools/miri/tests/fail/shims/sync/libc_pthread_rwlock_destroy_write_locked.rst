src/tools/miri/tests/fail/shims/sync/libc_pthread_rwlock_destroy_write_locked.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

fn main() {
    let rw = std::cell::UnsafeCell::new(libc::PTHREAD_RWLOCK_INITIALIZER);
    unsafe {
        assert_eq!(libc::pthread_rwlock_wrlock(rw.get()), 0);
        libc::pthread_rwlock_destroy(rw.get()); //~ ERROR: destroyed a locked rwlock
    }
}


