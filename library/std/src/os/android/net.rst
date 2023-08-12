library/std/src/os/android/net.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Android-specific networking functionality.

#![unstable(feature = "tcp_quickack", issue = "96256")]

#[unstable(feature = "unix_socket_abstract", issue = "85410")]
pub use crate::os::net::linux_ext::addr::SocketAddrExt;

#[unstable(feature = "tcp_quickack", issue = "96256")]
pub use crate::os::net::linux_ext::tcp::TcpStreamExt;


