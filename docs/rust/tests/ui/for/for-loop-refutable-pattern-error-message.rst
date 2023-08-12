tests/ui/for/for-loop-refutable-pattern-error-message.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for &1 in [1].iter() {} //~ ERROR refutable pattern in `for` loop binding
}


