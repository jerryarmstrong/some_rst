src/tools/miri/tests/fail/shims/sync/libc_pthread_rwlock_double_destroy.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

/// Test that destroying a pthread_rwlock twice fails, even without a check for number validity

fn main() {
    unsafe {
        let mut lock = libc::PTHREAD_RWLOCK_INITIALIZER;

        libc::pthread_rwlock_destroy(&mut lock);

        libc::pthread_rwlock_destroy(&mut lock);
        //~^ ERROR: Undefined Behavior: using uninitialized data, but this operation requires initialized memory
    }
}


