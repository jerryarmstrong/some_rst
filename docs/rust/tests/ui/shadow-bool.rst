tests/ui/shadow-bool.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

mod bar {
    pub trait QueryId {
        const SOME_PROPERTY: bool;
    }
}

use bar::QueryId;

#[allow(non_camel_case_types)]
pub struct bool;

impl QueryId for bool {
    const SOME_PROPERTY: core::primitive::bool = true;
}

fn main() {}


