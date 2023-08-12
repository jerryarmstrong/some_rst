tests/ui/const-generics/issues/issue-69654-run-pass.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Bar<T> {}
impl<T> Bar<T> for [u8; 7] {}

struct Foo<const N: usize> {}
impl<const N: usize> Foo<N>
where
    [u8; N]: Bar<[(); N]>,
{
    fn foo() {}
}

fn main() {
    Foo::foo();
}


