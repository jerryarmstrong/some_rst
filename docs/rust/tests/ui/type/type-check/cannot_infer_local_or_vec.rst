tests/ui/type/type-check/cannot_infer_local_or_vec.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = vec![];
    //~^ ERROR type annotations needed
}


