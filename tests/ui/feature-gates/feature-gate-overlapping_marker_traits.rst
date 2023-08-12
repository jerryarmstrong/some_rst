tests/ui/feature-gates/feature-gate-overlapping_marker_traits.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::{Debug, Display};

trait MyMarker {}

impl<T: Display> MyMarker for T {}
impl<T: Debug> MyMarker for T {}
//~^ ERROR E0119

fn main() {}


