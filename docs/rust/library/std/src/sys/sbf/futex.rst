library/std/src/sys/sbf/futex.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::sync::atomic::AtomicU32;
use crate::time::Duration;

pub fn futex_wait(_futex: &AtomicU32, _expected: u32, _timeout: Option<Duration>) -> bool {
    false
}

#[inline]
pub fn futex_wake(_futex: &AtomicU32) -> bool {
    false
}

#[inline]
pub fn futex_wake_all(_futex: &AtomicU32) {}


