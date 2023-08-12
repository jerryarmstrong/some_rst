src/std/src/sys/windows/thread_local_dtor.rs
============================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![unstable(feature = "thread_local_internals", issue = "none")]
#![cfg(target_thread_local)]

pub use crate::sys_common::thread_local_dtor::register_dtor_fallback as register_dtor;


