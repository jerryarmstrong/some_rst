tests/ui/type-inference/unbounded-associated-type.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    type A;
    fn foo(&self) -> Self::A {
        panic!()
    }
}

struct S<X>(std::marker::PhantomData<X>);

impl<X> T for S<X> {
   type A = X;
}

fn main() {
    S(std::marker::PhantomData).foo(); //~ ERROR type annotations needed
}


