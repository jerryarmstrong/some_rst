tests/ui/resolve/unboxed-closure-sugar-nonexistent-trait.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<F:Nonexist(isize) -> isize>(x: F) {}
//~^ ERROR cannot find trait `Nonexist`

type Typedef = isize;

fn g<F:Typedef(isize) -> isize>(x: F) {}
//~^ ERROR expected trait, found type alias `Typedef`

fn main() {}


