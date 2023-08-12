tests/ui/numbers-arithmetic/float-literal-inference.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct S {
    z: f64
}

pub fn main() {
    let x: f32 = 4.0;
    println!("{}", x);
    let y: f64 = 64.0;
    println!("{}", y);
    let z = S { z: 1.0 };
    println!("{}", z.z);
}


