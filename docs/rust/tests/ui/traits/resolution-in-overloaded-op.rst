tests/ui/traits/resolution-in-overloaded-op.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #12402 Operator overloading only considers the method name, not which trait is implemented

trait MyMul<Rhs, Res> {
    fn mul(&self, rhs: &Rhs) -> Res;
}

fn foo<T: MyMul<f64, f64>>(a: &T, b: f64) -> f64 {
    a * b //~ ERROR cannot multiply `&T` by `f64`
}

fn main() {}


