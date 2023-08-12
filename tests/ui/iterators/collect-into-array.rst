tests/ui/iterators/collect-into-array.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let whatever: [u32; 10] = (0..10).collect();
    //~^ ERROR an array of type `[u32; 10]` cannot be built directly from an iterator
    //~| NOTE try collecting into a `Vec<{integer}>`, then using `.try_into()`
    //~| NOTE required by a bound in `collect`
}


