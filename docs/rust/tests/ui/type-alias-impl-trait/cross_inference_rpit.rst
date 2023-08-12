tests/ui/type-alias-impl-trait/cross_inference_rpit.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn foo(b: bool) -> impl Copy {
    if b {
        return (5,6)
    }
    let x: (_, _) = foo(true);
    println!("{:?}", x);
    (1u32, 2u32)
}

fn main() {
    foo(false);
}


