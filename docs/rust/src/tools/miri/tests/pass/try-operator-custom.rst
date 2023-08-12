src/tools/miri/tests/pass/try-operator-custom.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert!(Ok::<i32, String>(42) == Ok(42));
}


