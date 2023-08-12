tests/ui/numbers-arithmetic/float.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let pi = 3.1415927f64;
    println!("{}", -pi * (pi + 2.0 / pi) - pi * 5.0);
    if pi == 5.0 || pi < 10.0 || pi <= 2.0 || pi != 22.0 / 7.0 || pi >= 10.0
           || pi > 1.0 {
        println!("yes");
    }
}


