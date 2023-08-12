tests/ui/macros/assert.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: with-generic-asset without-generic-asset
// [with-generic-asset] compile-flags: --cfg feature="generic_assert"

fn main() {
    assert!();  //~ ERROR requires a boolean expression
    assert!(struct); //~ ERROR expected expression
    debug_assert!(); //~ ERROR requires a boolean expression
    debug_assert!(struct); //~ ERROR expected expression
}


