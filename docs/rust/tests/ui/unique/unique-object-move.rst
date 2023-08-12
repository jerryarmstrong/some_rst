tests/ui/unique/unique-object-move.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Issue #5192

// pretty-expanded FIXME #23616

pub trait EventLoop { fn foo(&self) {} }

pub struct UvEventLoop {
    uvio: isize
}

impl EventLoop for UvEventLoop { }

pub fn main() {
    let loop_: Box<dyn EventLoop> = Box::new(UvEventLoop { uvio: 0 }) as Box<dyn EventLoop>;
    let _loop2_ = loop_;
}


