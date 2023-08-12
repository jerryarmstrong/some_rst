tests/ui/no_crate_type.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for issue 11256
#![crate_type]  //~ ERROR malformed `crate_type` attribute

fn main() {
    return
}


