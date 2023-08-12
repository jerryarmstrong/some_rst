tests/ui/const-generics/min_const_generics/const_default_first.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![allow(dead_code)]

struct Both<const N: usize=3, T> {
//~^ ERROR: generic parameters with a default must be
  v: T
}


