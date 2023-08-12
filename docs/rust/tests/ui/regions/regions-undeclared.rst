tests/ui/regions/regions-undeclared.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static c_x: &'blk isize = &22; //~ ERROR use of undeclared lifetime name `'blk`

enum EnumDecl {
    Foo(&'a isize), //~ ERROR use of undeclared lifetime name `'a`
    Bar(&'a isize), //~ ERROR use of undeclared lifetime name `'a`
}

fn fnDecl(x: &'a isize, //~ ERROR use of undeclared lifetime name `'a`
          y: &'a isize) //~ ERROR use of undeclared lifetime name `'a`
{}

fn main() {
}


