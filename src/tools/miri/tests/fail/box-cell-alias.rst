src/tools/miri/tests/fail/box-cell-alias.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-strict-provenance

// Taken from <https://github.com/rust-lang/unsafe-code-guidelines/issues/194#issuecomment-520934222>.

use std::cell::Cell;

fn helper(val: Box<Cell<u8>>, ptr: *const Cell<u8>) -> u8 {
    val.set(10);
    unsafe { (*ptr).set(20) }; //~ ERROR: does not exist in the borrow stack
    val.get()
}

fn main() {
    let val: Box<Cell<u8>> = Box::new(Cell::new(25));
    let ptr: *const Cell<u8> = &*val;
    let res = helper(val, ptr);
    assert_eq!(res, 20);
}


