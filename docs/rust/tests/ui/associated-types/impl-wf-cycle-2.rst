tests/ui/associated-types/impl-wf-cycle-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #79714

trait Grault {
    type A;
}

impl<T: Grault> Grault for (T,)
//~^ ERROR overflow evaluating the requirement `<(T,) as Grault>::A == _`
where
    Self::A: Copy,
{
    type A = ();
}

fn main() {}


