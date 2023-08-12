tests/ui/associated-consts/associated-const-trait-bound.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

trait ConstDefault {
    const DEFAULT: Self;
}

trait Foo: Sized {}

trait FooExt: Foo {
    type T: ConstDefault;
}

trait Bar<F: FooExt> {
    const T: F::T;
}

impl<F: FooExt> Bar<F> for () {
    const T: F::T = <F::T as ConstDefault>::DEFAULT;
}

fn main() {}


