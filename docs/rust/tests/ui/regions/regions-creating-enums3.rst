tests/ui/regions/regions-creating-enums3.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Ast<'a> {
    Num(usize),
    Add(&'a Ast<'a>, &'a Ast<'a>)
}

fn mk_add_bad1<'a,'b>(x: &'a Ast<'a>, y: &'b Ast<'b>) -> Ast<'a> {
    Ast::Add(x, y)
    //~^ ERROR lifetime may not live long enough
}

fn main() {
}


