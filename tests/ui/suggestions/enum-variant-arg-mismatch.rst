tests/ui/suggestions/enum-variant-arg-mismatch.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Sexpr<'a> {
    Ident(&'a str),
}

fn map<'a, F: Fn(String) -> Sexpr<'a>>(f: F) {}

fn main() {
    map(Sexpr::Ident);
    //~^ ERROR type mismatch in function arguments
}


