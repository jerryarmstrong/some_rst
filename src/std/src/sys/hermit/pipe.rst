src/std/src/sys/hermit/pipe.rs
==============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use crate::io::{self, IoSlice, IoSliceMut};
use crate::sys::Void;

pub struct AnonPipe(Void);

impl AnonPipe {
    pub fn read(&self, _buf: &mut [u8]) -> io::Result<usize> {
        match self.0 {}
    }

    pub fn read_vectored(&self, _bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
        match self.0 {}
    }

    pub fn is_read_vectored(&self) -> bool {
        match self.0 {}
    }

    pub fn write(&self, _buf: &[u8]) -> io::Result<usize> {
        match self.0 {}
    }

    pub fn write_vectored(&self, _bufs: &[IoSlice<'_>]) -> io::Result<usize> {
        match self.0 {}
    }

    pub fn is_write_vectored(&self) -> bool {
        match self.0 {}
    }

    pub fn diverge(&self) -> ! {
        match self.0 {}
    }
}

pub fn read2(p1: AnonPipe, _v1: &mut Vec<u8>, _p2: AnonPipe, _v2: &mut Vec<u8>) -> io::Result<()> {
    match p1.0 {}
}


