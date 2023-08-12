tests/ui/const-generics/type-dependent/type-mismatch.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min
struct R;

impl R {
    fn method<const N: u8>(&self) -> u8 { N }
}
fn main() {
    assert_eq!(R.method::<1u16>(), 1);
    //~^ ERROR mismatched types
}


