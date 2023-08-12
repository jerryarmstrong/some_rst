tests/ui/where-clauses/where-equality-constraints.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() where u8 = u16 {}
//~^ ERROR equality constraints are not yet supported in `where` clauses
fn g() where for<'a> &'static (u8,) == u16, {}
//~^ ERROR equality constraints are not yet supported in `where` clauses

fn main() {}


