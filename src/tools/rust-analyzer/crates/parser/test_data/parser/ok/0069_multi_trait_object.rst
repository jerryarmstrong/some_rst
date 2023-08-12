src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0069_multi_trait_object.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type Foo<'a> = &'a (dyn Send + Sync);
type Foo = *const (dyn Send + Sync);
type Foo = fn() -> (dyn Send + 'static);
fn main() {
    let b = (&a) as &(dyn Add<Other, Output = Addable> + Other);
}


