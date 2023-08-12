tests/ui/issues/issue-4830.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]

// pretty-expanded FIXME #23616

pub struct Scheduler {
    /// The event loop used to drive the scheduler and perform I/O
    event_loop: Box<isize>
}

pub fn main() { }


