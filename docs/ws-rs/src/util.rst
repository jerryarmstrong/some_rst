src/util.rs
===========

Last edited: 2018-12-06 12:44:12

Contents:

.. code-block:: rs

    //! The util module rexports some tools from mio in order to facilitate handling timeouts.

/// Used to identify some timed-out event.
pub use mio::Token;
/// A handle to a specific timeout.
pub use mio_extras::timer::Timeout;
#[cfg(any(feature = "ssl", feature = "nativetls"))]
/// TcpStream underlying the WebSocket
pub use mio::tcp::TcpStream;


