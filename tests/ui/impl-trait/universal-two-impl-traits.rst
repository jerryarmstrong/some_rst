tests/ui/impl-trait/universal-two-impl-traits.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

fn foo(x: impl Debug, y: impl Debug) -> String {
    let mut a = x;
    a = y; //~ ERROR mismatched
    format!("{:?}", a)
}

trait S<T> {}

fn much_universe<T: S<impl Debug>, U: IntoIterator<Item = impl Iterator<Item = impl Clone>>>(
    _: impl Debug + Clone,
) {
}

fn main() {}


