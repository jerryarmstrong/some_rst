src/tools/rustfmt/tests/target/issue_4257.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait<T> {
    type Type<'a>
    where
        T: 'a;
    fn foo(x: &T) -> Self::Type<'_>;
}
impl<T> Trait<T> for () {
    type Type<'a>
    where
        T: 'a,
    = &'a T;
    fn foo(x: &T) -> Self::Type<'_> {
        x
    }
}


