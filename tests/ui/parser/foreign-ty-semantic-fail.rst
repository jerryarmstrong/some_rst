tests/ui/parser/foreign-ty-semantic-fail.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

fn main() {}

extern "C" {
    type A: Ord;
    //~^ ERROR bounds on `type`s in `extern` blocks have no effect
    type B<'a> where 'a: 'static;
    //~^ ERROR `type`s inside `extern` blocks cannot have generic parameters
    //~| ERROR `type`s inside `extern` blocks cannot have `where` clauses
    type C<T: Ord> where T: 'static;
    //~^ ERROR `type`s inside `extern` blocks cannot have generic parameters
    //~| ERROR `type`s inside `extern` blocks cannot have `where` clauses
    type D = u8;
    //~^ ERROR incorrect `type` inside `extern` block

    type E: where;
}


