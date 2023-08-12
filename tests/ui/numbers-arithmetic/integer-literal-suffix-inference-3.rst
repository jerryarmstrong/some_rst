tests/ui/numbers-arithmetic/integer-literal-suffix-inference-3.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    println!("{}", std::mem::size_of_val(&1));
}


