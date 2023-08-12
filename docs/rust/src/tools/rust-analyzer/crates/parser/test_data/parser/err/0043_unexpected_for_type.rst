src/tools/rust-analyzer/crates/parser/test_data/parser/err/0043_unexpected_for_type.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type ForRef = for<'a> &'a u32;
type ForTup = for<'a> (&'a u32,);
type ForSlice = for<'a> [u32];
type ForForFn = for<'a> for<'b> fn(&'a i32, &'b i32);
fn for_for_for<T>()
where
    for<'a> for<'b> for<'c> fn(&'a T, &'b T, &'c T): Copy,
{
}


