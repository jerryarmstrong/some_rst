tests/ui/const-generics/trait-const-args.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Const<const N: usize>;
trait Foo<const N: usize> {}

impl<const N: usize> Foo<N> for Const<N> {}

fn foo_impl(_: impl Foo<3>) {}

fn foo_explicit<T: Foo<3>>(_: T) {}

fn foo_where<T>(_: T)
where
    T: Foo<3>,
{
}

fn main() {
    foo_impl(Const);
    foo_impl(Const::<3>);

    foo_explicit(Const);
    foo_explicit(Const::<3>);

    foo_where(Const);
    foo_where(Const::<3>);
}


