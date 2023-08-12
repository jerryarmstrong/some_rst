src/tools/miri/tests/fail/shims/sync/libc_pthread_condattr_double_destroy.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows

/// Test that destroying a pthread_condattr twice fails, even without a check for number validity

fn main() {
    unsafe {
        use core::mem::MaybeUninit;
        let mut attr = MaybeUninit::<libc::pthread_condattr_t>::uninit();

        libc::pthread_condattr_init(attr.as_mut_ptr());

        libc::pthread_condattr_destroy(attr.as_mut_ptr());

        libc::pthread_condattr_destroy(attr.as_mut_ptr());
        //~^ ERROR: Undefined Behavior: using uninitialized data, but this operation requires initialized memory
    }
}


