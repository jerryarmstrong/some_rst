tests/ui/wf/wf-array-elem-sized.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that array element types must be Sized. Issue #25692.


#![allow(dead_code)]

struct Foo {
    foo: [[u8]], //~ ERROR E0277
}


fn main() { }


