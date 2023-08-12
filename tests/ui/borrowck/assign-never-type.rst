tests/ui/borrowck/assign-never-type.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue 62165

// check-pass

#![feature(never_type)]

pub fn main() {
    loop {
        match None {
            None => return,
            Some(val) => val,
        };
    };
}


