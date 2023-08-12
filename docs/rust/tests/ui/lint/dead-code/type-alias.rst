tests/ui/lint/dead-code/type-alias.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(dead_code)]

type Used = u8;
type Unused = u8; //~ ERROR type alias `Unused` is never used

fn id(x: Used) -> Used { x }

fn main() {
    id(0);
}


