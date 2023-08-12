src/std/src/sys/bpf/thread_local_dtor.rs
========================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![cfg(target_thread_local)]
#![unstable(feature = "thread_local_internals", issue = "none")]

pub unsafe fn register_dtor(t: *mut u8, dtor: unsafe extern "C" fn(*mut u8)) {
    use crate::sys_common::thread_local_dtor::register_dtor_fallback;
    register_dtor_fallback(t, dtor);
}


