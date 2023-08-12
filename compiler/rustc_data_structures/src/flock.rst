compiler/rustc_data_structures/src/flock.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Simple file-locking apis for each OS.
//!
//! This is not meant to be in the standard library, it does nothing with
//! green/native threading. This is just a bare-bones enough solution for
//! librustdoc, it is not production quality at all.

#![allow(non_camel_case_types)]
#![allow(nonstandard_style)]

cfg_if! {
    if #[cfg(target_os = "linux")] {
        mod linux;
        use linux as imp;
    } else if #[cfg(unix)] {
        mod unix;
        use unix as imp;
    } else if #[cfg(windows)] {
        mod windows;
        use windows as imp;
    } else {
        mod unsupported;
        use unsupported as imp;
    }
}

pub use imp::Lock;


