tests/ui/lifetimes/lifetime-no-keyword.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<'a>(a: &'a isize) { }
fn bar(a: &'static isize) { }
fn baz<'let>(a: &'let isize) { } //~ ERROR lifetimes cannot use keyword names
//~^ ERROR lifetimes cannot use keyword names
fn zab<'self>(a: &'self isize) { } //~ ERROR lifetimes cannot use keyword names
//~^ ERROR lifetimes cannot use keyword names
fn main() { }


