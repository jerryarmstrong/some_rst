src/tools/miri/tests/fail/shims/sync/libc_pthread_rwlock_write_read_deadlock.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

use std::cell::UnsafeCell;
use std::sync::Arc;
use std::thread;

struct RwLock(UnsafeCell<libc::pthread_rwlock_t>);

unsafe impl Send for RwLock {}
unsafe impl Sync for RwLock {}

fn new_lock() -> Arc<RwLock> {
    Arc::new(RwLock(UnsafeCell::new(libc::PTHREAD_RWLOCK_INITIALIZER)))
}

fn main() {
    unsafe {
        let lock = new_lock();
        assert_eq!(libc::pthread_rwlock_rdlock(lock.0.get() as *mut _), 0);

        let lock_copy = lock.clone();
        thread::spawn(move || {
            assert_eq!(libc::pthread_rwlock_wrlock(lock_copy.0.get() as *mut _), 0); //~ ERROR: deadlock
        })
        .join()
        .unwrap();
    }
}


