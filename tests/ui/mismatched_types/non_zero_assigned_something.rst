tests/ui/mismatched_types/non_zero_assigned_something.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: std::num::NonZeroU64 = 1;
    //~^ ERROR mismatched types
    //~| HELP  consider calling `NonZeroU64::new`

    let _: Option<std::num::NonZeroU64> = 1;
    //~^ ERROR mismatched types
    //~| HELP  consider calling `NonZeroU64::new`
}


