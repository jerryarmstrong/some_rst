src/tools/miri/tests/pass/move-arg-3-unique.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]

pub fn main() {
    let x = box 10;
    let y = x;
    assert_eq!(*y, 10);
}


