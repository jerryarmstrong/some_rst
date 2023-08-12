tests/ui/const-generics/unify_with_nested_expr.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

fn foo<const N: usize>()
where
    [(); N + 1 + 1]:,
{
    bar();
    //~^ ERROR: type annotations
}

fn bar<const N: usize>()
where
    [(); N + 1]:,
{
}

fn main() {}


