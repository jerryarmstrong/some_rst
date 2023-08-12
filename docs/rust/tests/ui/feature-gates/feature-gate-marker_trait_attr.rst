tests/ui/feature-gates/feature-gate-marker_trait_attr.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::{Debug, Display};

#[marker] trait ExplicitMarker {}
//~^ ERROR the `#[marker]` attribute is an experimental feature

impl<T: Display> ExplicitMarker for T {}
impl<T: Debug> ExplicitMarker for T {}

fn main() {}


