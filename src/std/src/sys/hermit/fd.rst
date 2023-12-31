src/std/src/sys/hermit/fd.rs
============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![unstable(reason = "not public", issue = "none", feature = "fd")]

use crate::io::{self, ErrorKind, Read};
use crate::mem;
use crate::sys::cvt;
use crate::sys::hermit::abi;
use crate::sys_common::AsInner;

#[derive(Debug)]
pub struct FileDesc {
    fd: i32,
}

impl FileDesc {
    pub fn new(fd: i32) -> FileDesc {
        FileDesc { fd }
    }

    pub fn raw(&self) -> i32 {
        self.fd
    }

    /// Extracts the actual file descriptor without closing it.
    pub fn into_raw(self) -> i32 {
        let fd = self.fd;
        mem::forget(self);
        fd
    }

    pub fn read(&self, buf: &mut [u8]) -> io::Result<usize> {
        let result = unsafe { abi::read(self.fd, buf.as_mut_ptr(), buf.len()) };
        cvt(result as i32)
    }

    pub fn read_to_end(&self, buf: &mut Vec<u8>) -> io::Result<usize> {
        let mut me = self;
        (&mut me).read_to_end(buf)
    }

    pub fn write(&self, buf: &[u8]) -> io::Result<usize> {
        let result = unsafe { abi::write(self.fd, buf.as_ptr(), buf.len()) };
        cvt(result as i32)
    }

    pub fn duplicate(&self) -> io::Result<FileDesc> {
        self.duplicate_path(&[])
    }
    pub fn duplicate_path(&self, _path: &[u8]) -> io::Result<FileDesc> {
        Err(io::Error::new(ErrorKind::Other, "duplicate isn't supported"))
    }

    pub fn nonblocking(&self) -> io::Result<bool> {
        Ok(false)
    }

    pub fn set_cloexec(&self) -> io::Result<()> {
        Err(io::Error::new(ErrorKind::Other, "cloexec isn't supported"))
    }

    pub fn set_nonblocking(&self, _nonblocking: bool) -> io::Result<()> {
        Err(io::Error::new(ErrorKind::Other, "nonblocking isn't supported"))
    }
}

impl<'a> Read for &'a FileDesc {
    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
        (**self).read(buf)
    }
}

impl AsInner<i32> for FileDesc {
    fn as_inner(&self) -> &i32 {
        &self.fd
    }
}

impl Drop for FileDesc {
    fn drop(&mut self) {
        // Note that errors are ignored when closing a file descriptor. The
        // reason for this is that if an error occurs we don't actually know if
        // the file descriptor was closed or not, and if we retried (for
        // something like EINTR), we might close another valid file descriptor
        // (opened after we closed ours.
        let _ = unsafe { abi::close(self.fd) };
    }
}


