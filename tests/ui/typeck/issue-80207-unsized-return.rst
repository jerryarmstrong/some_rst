tests/ui/typeck/issue-80207-unsized-return.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Foo {
    fn do_stuff() -> Self;
}

trait Bar {
    type Output;
}

impl<T> Foo for dyn Bar<Output = T>
where
    Self: Sized,
{
    fn do_stuff() -> Self {
        todo!()
    }
}

fn main() {}


