tests/ui/typeck/typeck_type_placeholder_1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// This test checks that the `_` type placeholder works
// correctly for enabling type inference.


struct TestStruct {
    x: *const isize
}

unsafe impl Sync for TestStruct {}

static CONSTEXPR: TestStruct = TestStruct{ x: &413 };


pub fn main() {
    let x: Vec<_> = (0..5).collect();
    let expected: &[usize] = &[0,1,2,3,4];
    assert_eq!(x, expected);

    let x = (0..5).collect::<Vec<_>>();
    assert_eq!(x, expected);

    let y: _ = "hello";
    assert_eq!(y.len(), 5);

    let ptr: &usize = &5;
    let ptr2 = ptr as *const _;

    assert_eq!(ptr as *const usize as usize, ptr2 as usize);
}


