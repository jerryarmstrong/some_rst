tests/ui/for/for-loop-unconstrained-element-type.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `for` loops don't introduce artificial
// constraints on the type of the binding (`i`).
// Subtle changes in the desugaring can cause the
// type of elements in the vector to (incorrectly)
// fallback to `!` or `()`.

fn main() {
    for i in Vec::new() { } //~ ERROR type annotations needed
}


