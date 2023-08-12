src/tools/miri/src/shims/unix/mod.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod dlsym;
pub mod foreign_items;

mod fs;
mod sync;
mod thread;

mod android;
mod freebsd;
mod linux;
mod macos;

pub use fs::{DirHandler, FileHandler};

// Make up some constants.
const UID: u32 = 1000;


