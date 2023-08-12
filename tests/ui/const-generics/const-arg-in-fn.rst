tests/ui/const-generics/const-arg-in-fn.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn const_u32_identity<const X: u32>() -> u32 {
    X
}

 fn main() {
    let val = const_u32_identity::<18>();
    assert_eq!(val, 18);
}


