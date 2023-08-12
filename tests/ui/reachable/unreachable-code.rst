tests/ui/reachable/unreachable-code.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_code)]
#![allow(unused_variables)]

fn main() {
  loop{}

  let a = 3; //~ ERROR: unreachable statement
}


