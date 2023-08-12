tests/ui/type/type-check/cannot_infer_local_or_array.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = []; //~ ERROR type annotations needed
}


