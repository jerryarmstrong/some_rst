src/std/src/sys_common/at_exit_imp.rs
=====================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    //! Implementation of running at_exit routines
//!
//! Documentation can be found on the `rt::at_exit` function.
#![cfg(not(target_arch = "bpf"))]

use crate::mem;
use crate::ptr;
use crate::sys_common::mutex::StaticMutex;

type Queue = Vec<Box<dyn FnOnce()>>;

// NB these are specifically not types from `std::sync` as they currently rely
// on poisoning and this module needs to operate at a lower level than requiring
// the thread infrastructure to be in place (useful on the borders of
// initialization/destruction).
// It is UB to attempt to acquire this mutex reentrantly!
#[cfg(not(target_arch = "bpf"))]
static LOCK: StaticMutex = StaticMutex::new();
#[cfg(not(target_arch = "bpf"))]
static mut QUEUE: *mut Queue = ptr::null_mut();

const DONE: *mut Queue = 1_usize as *mut _;

// The maximum number of times the cleanup routines will be run. While running
// the at_exit closures new ones may be registered, and this count is the number
// of times the new closures will be allowed to register successfully. After
// this number of iterations all new registrations will return `false`.
const ITERS: usize = 10;

unsafe fn init() -> bool {
    #[cfg(not(target_arch = "bpf"))]
    {
        if QUEUE.is_null() {
            let state: Box<Queue> = box Vec::new();
            QUEUE = Box::into_raw(state);
        } else if QUEUE == DONE {
            // can't re-init after a cleanup
            return false;
        }
    }

    true
}

pub fn cleanup() {
    // TODO causes LLVM to crash when compiling for BPF, not needed to BPF anyway for commented out
    #[cfg(not(target_arch = "bpf"))]
    for i in 1..=ITERS {
        unsafe {
            let queue = {
                let _guard = LOCK.lock();
                crate::mem::replace(&mut QUEUE, if i == ITERS { DONE } else { ptr::null_mut() })
            };

            // make sure we're not recursively cleaning up
            assert!(queue != DONE);

            // If we never called init, not need to cleanup!
            if !queue.is_null() {
                let queue: Box<Queue> = Box::from_raw(queue);
                for to_run in *queue {
                    // We are not holding any lock, so reentrancy is fine.
                    to_run();
                }
            }
        }
    }
}

pub fn push(f: Box<dyn FnOnce()>) -> bool {
    #[cfg(not(target_arch = "bpf"))]
    unsafe {
        let _guard = LOCK.lock();
        if init() {
            // We are just moving `f` around, not calling it.
            // There is no possibility of reentrancy here.
            (*QUEUE).push(f);
            true
        } else {
            false
        }
    }
    #[cfg(target_arch = "bpf")]
    {
        true
    }
}


