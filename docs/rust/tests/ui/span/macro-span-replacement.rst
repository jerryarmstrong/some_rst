tests/ui/span/macro-span-replacement.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![warn(unused)]

macro_rules! m {
    ($a:tt $b:tt) => {
        $b $a; //~ WARN struct `S` is never constructed
    }
}

fn main() {
    m!(S struct);
}


