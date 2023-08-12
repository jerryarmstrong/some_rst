src/tools/miri/tests/pass/drop_empty_slice.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]

fn main() {
    // With the nested Vec, this is calling Offset(Unique::empty(), 0) on drop.
    let args: Vec<Vec<i32>> = Vec::new();
    let _val = box args;
}


