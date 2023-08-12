library/std/src/sys/sbf/thread.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::ffi::CStr;
use crate::io;
use crate::num::NonZeroUsize;
use crate::sys::{unsupported, Void};
use crate::time::Duration;

pub struct Thread(Void);

impl Thread {
    // unsafe: see thread::Builder::spawn_unchecked for safety requirements
    pub unsafe fn new(_stack: usize, _p: Box<dyn FnOnce()>)
        -> io::Result<Thread>
    {
        unsupported()
    }

    pub fn yield_now() {
        // do nothing
    }

    pub fn set_name(_name: &CStr) {
        // nope
    }

    pub fn sleep(_dur: Duration) {
        panic!("can't sleep");
    }

    pub fn join(self) {
        match self.0 {}
    }
}

pub fn available_parallelism() -> io::Result<NonZeroUsize> {
    unsupported()
}


