src/std/src/sys/bpf/condvar.rs
==============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use crate::sys::mutex::Mutex;
use crate::time::Duration;

pub struct Condvar { }

pub type MovableCondvar = Box<Condvar>;

impl Condvar {
    pub const fn new() -> Condvar {
        Condvar { }
    }

    #[inline]
    pub unsafe fn init(&mut self) {}

    #[inline]
    pub unsafe fn notify_one(&self) {
    }

    #[inline]
    pub unsafe fn notify_all(&self) {
    }

    pub unsafe fn wait(&self, _mutex: &Mutex) {
        panic!("can't block with web assembly")
    }

    pub unsafe fn wait_timeout(&self, _mutex: &Mutex, _dur: Duration) -> bool {
        panic!("can't block with web assembly");
    }

    #[inline]
    pub unsafe fn destroy(&self) {
    }
}


