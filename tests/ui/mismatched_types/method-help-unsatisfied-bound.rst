tests/ui/mismatched_types/method-help-unsatisfied-bound.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

fn main() {
    let a: Result<(), Foo> = Ok(());
    a.unwrap();
    //~^ ERROR `Foo` doesn't implement `Debug`
}


