tests/ui/issues/issue-43420-no-over-suggest.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that we substitute type parameters before we suggest anything - otherwise
// we would suggest function such as `as_slice` for the `&[u16]`.

fn foo(b: &[u16]) {}

fn main() {
    let a: Vec<u8> = Vec::new();
    foo(&a); //~ ERROR mismatched types
}


