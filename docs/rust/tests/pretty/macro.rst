tests/pretty/macro.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

#![feature(decl_macro)]

pub(crate) macro mac { ($arg : expr) => { $arg + $arg } }

fn main() {}


