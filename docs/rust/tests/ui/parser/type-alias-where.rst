tests/ui/parser/type-alias-where.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

// Fine, but lints as unused
type Foo where u32: Copy = ();
// Not fine.
type Bar = () where u32: Copy;
//~^ ERROR where clauses are not allowed
type Baz = () where;
//~^ ERROR where clauses are not allowed

fn main() {}


