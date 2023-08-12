src/tools/miri/tests/fail/shims/sync/libc_pthread_mutex_double_destroy.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

/// Test that destroying a pthread_mutex twice fails, even without a check for number validity

fn main() {
    unsafe {
        use core::mem::MaybeUninit;

        let mut attr = MaybeUninit::<libc::pthread_mutexattr_t>::uninit();
        libc::pthread_mutexattr_init(attr.as_mut_ptr());

        let mut mutex = MaybeUninit::<libc::pthread_mutex_t>::uninit();

        libc::pthread_mutex_init(mutex.as_mut_ptr(), attr.as_ptr());

        libc::pthread_mutex_destroy(mutex.as_mut_ptr());

        libc::pthread_mutex_destroy(mutex.as_mut_ptr());
        //~^ ERROR: Undefined Behavior: using uninitialized data, but this operation requires initialized memory
    }
}


