src/std/src/sys/windows/stack_overflow_uwp.rs
=============================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![cfg_attr(test, allow(dead_code))]

pub struct Handler;

impl Handler {
    pub fn new() -> Handler {
        Handler
    }
}

pub unsafe fn init() {}

pub unsafe fn cleanup() {}


