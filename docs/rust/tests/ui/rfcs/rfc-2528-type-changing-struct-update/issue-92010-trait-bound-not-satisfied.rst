tests/ui/rfcs/rfc-2528-type-changing-struct-update/issue-92010-trait-bound-not-satisfied.rs
===========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
struct P<T> {
    x: T,
    y: f64,
}

impl<T> P<T> {
    fn y(&self, y: f64) -> Self { P{y, .. self.clone() } }
                                       //~^ mismatched types [E0308]
}

fn main() {}


