tests/ui/specialization/defaultimpl/specialization-wfcheck.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that a default impl still has to have a WF trait ref.

#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

trait Foo<'a, T: Eq + 'a> { }

default impl<U> Foo<'static, U> for () {}
//~^ ERROR the trait bound `U: Eq` is not satisfied

fn main(){}


