tests/ui/associated-types/normalization-probe-cycle.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #77656

// check-pass

trait Value: PartialOrd {}

impl<T: PartialOrd> Value for T {}

trait Distance
where
    Self: PartialOrd<<Self as Distance>::Value>,
    Self: PartialOrd,
{
    type Value: Value;
}

impl<T: Value> Distance for T {
    type Value = T;
}

trait Proximity<T = Self> {
    type Distance: Distance;
}

fn main() {}


