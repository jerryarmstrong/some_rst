tests/ui/closures/supertrait-hint-cycle-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Foo<'a> {
    type Input;
}

impl<F: Fn(u32)> Foo<'_> for F {
    type Input = u32;
}

trait SuperFn: for<'a> Foo<'a> + for<'a> Fn(<Self as Foo<'a>>::Input) {}
impl<T> SuperFn for T where T: for<'a> Fn(<Self as Foo<'a>>::Input) + for<'a> Foo<'a> {}

fn needs_super(_: impl SuperFn) {}

fn main() {
    needs_super(|_: u32| {});
}


