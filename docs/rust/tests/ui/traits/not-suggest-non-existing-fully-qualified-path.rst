tests/ui/traits/not-suggest-non-existing-fully-qualified-path.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<T>(T);
struct B;

trait I<T> {}
impl I<i32> for B {}
impl I<u32> for B {}

trait V<U> {
    fn method(self) -> U;
}

impl<T, U> V<U> for A<T>
where
    T: I<U>,
{
    fn method(self) -> U { unimplemented!() }
}

fn main() {
    let a = A(B);
    a.method();
    //~^ ERROR type annotations needed
    //~| ERROR type annotations needed
}


