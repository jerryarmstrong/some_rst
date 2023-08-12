tests/ui/consts/const-block-cross-crate-fn.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cci_const_block.rs


extern crate cci_const_block;

pub fn main() {
    assert_eq!(cci_const_block::BLOCK_FN_DEF(390), 400);
}


