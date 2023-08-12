tests/ui/associated-type-bounds/assoc-type-bound-through-where-clause.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `where Self::Output: Copy` is turned into a bound on `Op::Output`.

//check-pass

trait Op
where
    Self::Output: Copy,
{
    type Output;
}

fn duplicate<T: Op>(x: T::Output) -> (T::Output, T::Output) {
    (x, x)
}

fn main() {}


