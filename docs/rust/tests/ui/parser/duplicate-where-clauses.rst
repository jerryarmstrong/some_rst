tests/ui/parser/duplicate-where-clauses.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A where (): Sized where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

fn b() where (): Sized where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

enum C where (): Sized where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

struct D where (): Sized, where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

fn e() where (): Sized, where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

enum F where (): Sized, where (): Sized {}
//~^ ERROR cannot define duplicate `where` clauses on an item

fn main() {}


