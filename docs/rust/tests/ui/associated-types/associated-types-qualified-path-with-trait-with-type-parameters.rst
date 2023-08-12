tests/ui/associated-types/associated-types-qualified-path-with-trait-with-type-parameters.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait Foo<T> {
    type Bar;
    fn get_bar() -> <Self as Foo<T>>::Bar;
}

fn main() { }


