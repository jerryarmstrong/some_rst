tests/ui/auto-traits/bad-generics-on-dyn.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]

auto trait Trait1<'a> {}
//~^ ERROR auto traits cannot have generic parameters

fn f<'a>(x: &dyn Trait1<'a>)
{}

fn main() {
    f(&1);
}


