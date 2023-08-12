tests/ui/proc-macro/macro-rules-derive.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:first-second.rs

extern crate first_second;
use first_second::*;

macro_rules! produce_it {
    ($name:ident) => {
        #[first]
        struct $name {
            field: MissingType //~ ERROR cannot find type
        }
    }
}

produce_it!(MyName);

fn main() {
    println!("Hello, world!");
}


