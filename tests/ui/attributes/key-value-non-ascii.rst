tests/ui/attributes/key-value-non-ascii.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_dummy = b"ﬃ.rs"] //~ ERROR non-ASCII character in byte string literal
fn main() {}


