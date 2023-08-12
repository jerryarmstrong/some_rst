src/tools/rust-analyzer/crates/parser/test_data/parser/err/0024_many_type_parens.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T: (Copy) + (?Sized) + (for<'a> Trait<'a>)>() {}

fn main() {
    let _: Box<(Copy) + (?Sized) + (for<'a> Trait<'a>)>;
    let _: Box<(?Sized) + (for<'a> Trait<'a>) + (Copy)>;
    let _: Box<(for<'a> Trait<'a>) + (Copy) + (?Sized)>;
}


