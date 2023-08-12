tests/ui/mismatched_types/normalize-fn-sig.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Bar;
}

impl<T> Foo for T {
    type Bar = i32;
}

fn foo<T>(_: <T as Foo>::Bar, _: &'static <T as Foo>::Bar) {}

fn needs_i32_ref_fn(_: fn(&'static i32, i32)) {}

fn main() {
    needs_i32_ref_fn(foo::<()>);
    //~^ ERROR mismatched types
}


