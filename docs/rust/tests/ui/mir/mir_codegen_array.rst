tests/ui/mir/mir_codegen_array.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]
fn into_inner() -> [u64; 1024] {
    let mut x = 10 + 20;
    [x; 1024]
}

fn main(){
    let x: &[u64] = &[30; 1024];
    assert_eq!(&into_inner()[..], x);
}


