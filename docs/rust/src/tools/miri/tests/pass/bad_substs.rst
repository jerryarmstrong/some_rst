src/tools/miri/tests/pass/bad_substs.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let f: fn(i32) -> Option<i32> = Some::<i32>;
    f(42);
}


