tests/ui/illegal-sized-bound/mutability-mismatch-arg.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn test(t: &dyn Iterator<Item=&u64>) -> u64 {
     *t.min().unwrap() //~ ERROR the `min` method cannot be invoked on
}

fn main() {
     let array = [0u64];
     test(&mut array.iter());
}


