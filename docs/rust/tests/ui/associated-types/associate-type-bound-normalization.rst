tests/ui/associated-types/associate-type-bound-normalization.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we normalize bounds on associated types before checking them
// as candidates.

// check-pass

trait Mul<T> {
    type Output;
}

trait Matrix: Mul<<Self as Matrix>::Row, Output = ()> {
    type Row;

    type Transpose: Matrix<Row = Self::Row>;
}

fn is_mul<S, T: Mul<S, Output = ()>>() {}

fn f<T: Matrix>() {
    // The unnormalized bound on `T::Transpose` is
    // `Mul<<T::Transpose as Matrix>::Row` which has to be normalized to be
    // equal to `T::Row`.
    is_mul::<T::Row, T::Transpose>();
}

fn main() {}


