tests/rustdoc/auxiliary/issue-100204-aux.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="first"]

pub mod prelude {
    pub use crate::Bot;
}

pub struct Bot;

impl Bot {
    pub fn new() -> Bot {
        Bot
    }
}


