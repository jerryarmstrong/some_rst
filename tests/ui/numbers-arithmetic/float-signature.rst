tests/ui/numbers-arithmetic/float-signature.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


pub fn main() {
    fn foo(n: f64) -> f64 { return n + 0.12345; }
    let n: f64 = 0.1;
    let m: f64 = foo(n);
    println!("{}", m);
}


