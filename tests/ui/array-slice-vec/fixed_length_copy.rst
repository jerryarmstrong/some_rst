tests/ui/array-slice-vec/fixed_length_copy.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


pub fn main() {
    let arr = [1,2,3];
    let arr2 = arr;
    assert_eq!(arr[1], 2);
    assert_eq!(arr2[2], 3);
}


