tests/ui/parser/trailing-plus-in-bounds.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(bare_trait_objects)]

use std::fmt::Debug;

fn main() {
    let x: Box<Debug+> = Box::new(3) as Box<Debug+>; // Trailing `+` is OK
}


