tests/incremental/change_name_of_static_in_fn.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions:rpass1 rpass2 rpass3

// See issue #57692.

#![allow(warnings)]

fn main() {
    #[cfg(rpass1)]
    {
        static map: u64 = 0;
    }
    #[cfg(not(rpass1))]
    {
        static MAP: u64 = 0;
    }
}


