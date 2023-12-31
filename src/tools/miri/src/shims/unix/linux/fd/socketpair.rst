src/tools/miri/src/shims/unix/linux/fd/socketpair.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::*;

use crate::shims::unix::fs::FileDescriptor;

use std::io;

/// Pair of connected sockets.
///
/// We currently don't allow sending any data through this pair, so this can be just a dummy.
#[derive(Debug)]
pub struct SocketPair;

impl FileDescriptor for SocketPair {
    fn name(&self) -> &'static str {
        "socketpair"
    }

    fn dup(&mut self) -> io::Result<Box<dyn FileDescriptor>> {
        Ok(Box::new(SocketPair))
    }

    fn is_tty(&self) -> bool {
        false
    }

    fn close<'tcx>(
        self: Box<Self>,
        _communicate_allowed: bool,
    ) -> InterpResult<'tcx, io::Result<i32>> {
        Ok(Ok(0))
    }
}


