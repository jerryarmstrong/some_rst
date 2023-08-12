tests/codegen/auxiliary/thread_local_aux.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

use std::cell::Cell;

thread_local!(pub static A: Cell<u64> = const { Cell::new(0) });


