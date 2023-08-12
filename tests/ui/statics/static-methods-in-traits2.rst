tests/ui/statics/static-methods-in-traits2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub trait Number: NumConv {
    fn from<T:Number>(n: T) -> Self;
}

impl Number for f64 {
    fn from<T:Number>(n: T) -> f64 { n.to_float() }
}

pub trait NumConv {
    fn to_float(&self) -> f64;
}

impl NumConv for f64 {
    fn to_float(&self) -> f64 { *self }
}

pub fn main() {
    let _: f64 = Number::from(0.0f64);
}


