tests/ui/parser/bounds-obj-parens.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(bare_trait_objects)]

type A = Box<(Fn(u8) -> u8) + 'static + Send + Sync>; // OK (but see #39318)

fn main() {}


