tests/ui/suggestions/boxed-variant-field.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Ty {
    Unit,
    List(Box<Ty>),
}

fn foo(x: Ty) -> Ty {
    match x {
        Ty::Unit => Ty::Unit,
        Ty::List(elem) => foo(elem),
        //~^ ERROR mismatched types
        //~| HELP consider unboxing the value
    }
}

fn main() {}


