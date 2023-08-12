library/std/src/sys/sbf/rwlock.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::cell::UnsafeCell;

pub struct RwLock {
    mode: UnsafeCell<isize>,
}

pub type MovableRwLock = RwLock;

unsafe impl Send for RwLock {}
unsafe impl Sync for RwLock {} // no threads on SBF

impl RwLock {
    pub const fn new() -> RwLock {
        RwLock {
            mode: UnsafeCell::new(0),
        }
    }

    #[inline]
    pub unsafe fn read(&self) {
        let mode = self.mode.get();
        if *mode >= 0 {
            *mode += 1;
        } else {
            rtabort!("rwlock locked for writing");
        }
    }

    #[inline]
    pub unsafe fn try_read(&self) -> bool {
        let mode = self.mode.get();
        if *mode >= 0 {
            *mode += 1;
            true
        } else {
            false
        }
    }

    #[inline]
    pub unsafe fn write(&self) {
        let mode = self.mode.get();
        if *mode == 0 {
            *mode = -1;
        } else {
            rtabort!("rwlock locked for reading")
        }
    }

    #[inline]
    pub unsafe fn try_write(&self) -> bool {
        let mode = self.mode.get();
        if *mode == 0 {
            *mode = -1;
            true
        } else {
            false
        }
    }

    #[inline]
    pub unsafe fn read_unlock(&self) {
        *self.mode.get() -= 1;
    }

    #[inline]
    pub unsafe fn write_unlock(&self) {
        *self.mode.get() += 1;
    }
}


