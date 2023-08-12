tests/ui/imports/no-std-inject.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]

extern crate core; //~ ERROR: the name `core` is defined multiple times
extern crate std;

fn main() {}


