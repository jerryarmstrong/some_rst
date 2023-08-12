src/tools/rustfmt/tests/target/issue-5009/1_minimum_example.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // the "in" inside the pattern produced invalid syntax
    for variable_in_here /* ... */ in 0..1 {}
}


