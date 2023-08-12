tests/ui/suggestions/issue-71394-no-from-impl.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let data: &[u8] = &[0; 10];
    let _: &[i8] = data.into();
    //~^ ERROR the trait bound `&[i8]: From<&[u8]>` is not satisfied
}


