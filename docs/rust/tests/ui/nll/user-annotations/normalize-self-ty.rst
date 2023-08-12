tests/ui/nll/user-annotations/normalize-self-ty.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #55183: check a case where the self type from
// the inherent impl requires normalization to be equal to the
// user-provided type.
//
// check-pass

trait Mirror {
    type Me;
}

impl<T> Mirror for T {
    type Me = T;
}

struct Foo<A, B>(A, B);

impl<A> Foo<A, <A as Mirror>::Me> {
    fn m(_: A) { }
}

fn main() {
    <Foo<&'static u32, &u32>>::m(&22);
}


