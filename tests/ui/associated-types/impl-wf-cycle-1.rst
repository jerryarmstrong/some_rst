tests/ui/associated-types/impl-wf-cycle-1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #79714

trait Baz {}
impl Baz for () {}
impl<T> Baz for (T,) {}

trait Fiz {}
impl Fiz for bool {}

trait Grault {
    type A;
    type B;
}

impl<T: Grault> Grault for (T,)
//~^ ERROR overflow evaluating the requirement `<(T,) as Grault>::A == _`
where
    Self::A: Baz,
    Self::B: Fiz,
{
    type A = ();
    type B = bool;
}

fn main() {
    let x: <(_,) as Grault>::A = ();
}


