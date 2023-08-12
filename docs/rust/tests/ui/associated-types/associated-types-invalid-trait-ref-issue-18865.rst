tests/ui/associated-types/associated-types-invalid-trait-ref-issue-18865.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we report an error if the trait ref in a qualified type
// uses invalid type arguments.

trait Foo<T> {
    type Bar;
    fn get_bar(&self) -> Self::Bar;
}

fn f<T:Foo<isize>>(t: &T) {
    let u: <T as Foo<usize>>::Bar = t.get_bar();
    //~^ ERROR the trait bound `T: Foo<usize>` is not satisfied
}

fn main() { }


