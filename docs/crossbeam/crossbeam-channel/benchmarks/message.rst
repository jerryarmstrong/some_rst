crossbeam-channel/benchmarks/message.rs
=======================================

Last edited: 2022-07-31 15:42:50

Contents:

.. code-block:: rs

    use std::fmt;

const LEN: usize = 1;

#[derive(Clone, Copy)]
pub struct Message(pub [usize; LEN]);

impl fmt::Debug for Message {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.pad("Message")
    }
}

#[inline]
pub fn new(num: usize) -> Message {
    Message([num; LEN])
}


