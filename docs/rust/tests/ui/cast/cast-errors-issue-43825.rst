tests/ui/cast/cast-errors-issue-43825.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let error = error; //~ ERROR cannot find value `error`

    // These used to cause errors.
    0 as f32;
    0.0 as u32;
}


