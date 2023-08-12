library/std/src/os/net/linux_ext/mod.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Linux and Android-specific networking functionality.

#![doc(cfg(any(target_os = "linux", target_os = "android")))]

#[unstable(feature = "unix_socket_abstract", issue = "85410")]
pub(crate) mod addr;

#[unstable(feature = "tcp_quickack", issue = "96256")]
pub(crate) mod tcp;

#[cfg(test)]
mod tests;


