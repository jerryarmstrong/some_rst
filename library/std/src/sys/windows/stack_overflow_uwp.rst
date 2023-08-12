library/std/src/sys/windows/stack_overflow_uwp.rs
=================================================

Last edited: 2023-03-30 20:35:59

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


