src/tools/miri/tests/pass/available-parallelism.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(std::thread::available_parallelism().unwrap().get(), 1);
}


