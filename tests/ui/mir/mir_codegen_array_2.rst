tests/ui/mir/mir_codegen_array_2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn into_inner(x: u64) -> [u64; 1024] {
    [x; 2*4*8*16]
}

fn main(){
    let x: &[u64] = &[42; 1024];
    assert_eq!(&into_inner(42)[..], x);
}


