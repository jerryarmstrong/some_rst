src/std/src/sys_common/condvar.rs
=================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    use crate::sys::condvar as imp;
use crate::sys::mutex as mutex_imp;
use crate::sys_common::mutex::MovableMutex;
use crate::time::Duration;

mod check;

type CondvarCheck = <mutex_imp::MovableMutex as check::CondvarCheck>::Check;

/// An OS-based condition variable.
pub struct Condvar {
    inner: imp::MovableCondvar,
    check: CondvarCheck,
}

impl Condvar {
    /// Creates a new condition variable for use.
    pub fn new() -> Self {
        let mut c = imp::MovableCondvar::from(imp::Condvar::new());
        unsafe { c.init() };
        Self { inner: c, check: CondvarCheck::new() }
    }

    /// Signals one waiter on this condition variable to wake up.
    #[inline]
    pub fn notify_one(&self) {
        unsafe { self.inner.notify_one() };
    }

    /// Awakens all current waiters on this condition variable.
    #[inline]
    pub fn notify_all(&self) {
        unsafe { self.inner.notify_all() };
    }

    /// Waits for a signal on the specified mutex.
    ///
    /// Behavior is undefined if the mutex is not locked by the current thread.
    ///
    /// May panic if used with more than one mutex.
    #[inline]
    pub unsafe fn wait(&self, mutex: &MovableMutex) {
        self.check.verify(mutex);
        self.inner.wait(mutex.raw())
    }

    /// Waits for a signal on the specified mutex with a timeout duration
    /// specified by `dur` (a relative time into the future).
    ///
    /// Behavior is undefined if the mutex is not locked by the current thread.
    ///
    /// May panic if used with more than one mutex.
    #[inline]
    pub unsafe fn wait_timeout(&self, mutex: &MovableMutex, dur: Duration) -> bool {
        self.check.verify(mutex);
        self.inner.wait_timeout(mutex.raw(), dur)
    }
}

impl Drop for Condvar {
    fn drop(&mut self) {
        unsafe { self.inner.destroy() };
    }
}


