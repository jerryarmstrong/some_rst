tests/ui/stability-attribute/missing-stability-attr-at-top-level.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
//~^ ERROR module has missing stability attribute

fn main() {}


