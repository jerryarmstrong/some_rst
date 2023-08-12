tests/ui/typeck/issue-90804-incorrect-reference-suggestion.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Do not suggest referencing the parameter to `check`

trait Marker<T> {}

impl<T> Marker<i32> for T {}

pub fn check<T: Marker<u32>>(_: T) {}

pub fn main() {
    check::<()>(()); //~ ERROR [E0277]
}


