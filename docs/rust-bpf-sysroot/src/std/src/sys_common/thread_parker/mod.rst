src/std/src/sys_common/thread_parker/mod.rs
===========================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    cfg_if::cfg_if! {
    if #[cfg(any(
        target_os = "linux",
        target_os = "android",
        all(target_arch = "wasm32", target_feature = "atomics"),
    ))] {
        mod futex;
        pub use futex::Parker;
    } else if #[cfg(windows)] {
        pub use crate::sys::thread_parker::Parker;
    } else {
        mod generic;
        pub use generic::Parker;
    }
}


