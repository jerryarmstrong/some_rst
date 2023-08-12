tests/ui/inference/cannot-infer-closure.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = |a: (), b: ()| {
        Err(a)?;
        Ok(b)
        //~^ ERROR type annotations needed
    };
}


