library/std/src/sys/sgx/thread_parking.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::abi::usercalls;
use crate::io::ErrorKind;
use crate::time::Duration;
use fortanix_sgx_abi::{EV_UNPARK, WAIT_INDEFINITE};

pub type ThreadId = fortanix_sgx_abi::Tcs;

pub use super::abi::thread::current;

pub fn park(_hint: usize) {
    usercalls::wait(EV_UNPARK, WAIT_INDEFINITE).unwrap();
}

pub fn park_timeout(dur: Duration, _hint: usize) {
    let timeout = u128::min(dur.as_nanos(), WAIT_INDEFINITE as u128 - 1) as u64;
    if let Err(e) = usercalls::wait(EV_UNPARK, timeout) {
        assert!(matches!(e.kind(), ErrorKind::TimedOut | ErrorKind::WouldBlock))
    }
}

pub fn unpark(tid: ThreadId, _hint: usize) {
    let _ = usercalls::send(EV_UNPARK, Some(tid));
}


