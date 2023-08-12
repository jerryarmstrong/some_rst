tests/ui/const-generics/type-dependent/simple.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct R;

impl R {
    fn method<const N: u8>(&self) -> u8 { N }
}
fn main() {
    assert_eq!(R.method::<1u8>(), 1);
}


