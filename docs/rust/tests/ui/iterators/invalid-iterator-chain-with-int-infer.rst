tests/ui/iterators/invalid-iterator-chain-with-int-infer.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = Some(()).iter().map(|()| 1).sum::<f32>();
    //~^ ERROR a value of type `f32` cannot be made by summing an iterator over elements of type `{integer}`
}


