tests/ui/associated-types/associated-types-projection-in-where-clause.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// Test a where clause that uses a non-normalized projection type.

// pretty-expanded FIXME #23616

trait Int
{
    type T;

    fn dummy(&self) { }
}

trait NonZero
{
    fn non_zero(self) -> bool;
}

fn foo<I:Int<T=J>,J>(t: I) -> bool
    where <I as Int>::T : NonZero
    //    ^~~~~~~~~~~~~ canonical form is just J
{
    bar::<J>()
}

fn bar<NZ:NonZero>() -> bool { true }

fn main ()
{
}


