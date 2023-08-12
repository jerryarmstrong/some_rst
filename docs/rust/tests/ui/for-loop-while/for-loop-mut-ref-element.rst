tests/ui/for-loop-while/for-loop-mut-ref-element.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests that for loops can bind elements as mutable references

fn main() {
    for ref mut _a in std::iter::once(true) {}
}


