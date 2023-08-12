tests/ui/associated-types/normalize-cycle-in-eval-no-region.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Case that the fix for #74868 also allowed to compile

// check-pass

trait BoxedDsl {
    type Output;
}

impl<T> BoxedDsl for T
where
    T: BoxedDsl,
{
    type Output = <T as BoxedDsl>::Output;
}

trait HandleUpdate {}

impl<T> HandleUpdate for T where T: BoxedDsl<Output = ()> {}

fn main() {}


