tests/ui/underscore-imports/unused-2018.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![deny(unused_imports)]

mod multi_segment {
    use core::any; //~ ERROR unused import: `core::any`
}

mod single_segment {
    use core; //~ ERROR unused import: `core`
}

mod single_segment_underscore {
    use core as _; // OK
}

fn main() {}


