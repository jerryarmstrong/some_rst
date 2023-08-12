src/tools/miri/tests/fail/unreachable.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    unsafe { std::hint::unreachable_unchecked() } //~ERROR: entering unreachable code
}


