tests/ui/associated-types/wf-cycle.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait A {
    type U: Copy;
}

trait B where
    <Self::V as A>::U: Copy,
{
    type V: A;
}

fn main() {}


