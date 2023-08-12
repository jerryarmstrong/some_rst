tests/ui/impl-trait/universal_wrong_bounds.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Display;

fn foo(f: impl Display + Clone) -> String {
    wants_debug(f);
    wants_display(f);
    wants_clone(f);
}

fn wants_debug(g: impl Debug) { } //~ ERROR expected trait, found derive macro `Debug`
fn wants_display(g: impl Debug) { } //~ ERROR expected trait, found derive macro `Debug`
fn wants_clone(g: impl Clone) { }

fn main() {}


