tests/ui-fulldeps/internal-lints/diagnostics_incorrect.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options

#![feature(rustc_attrs)]

#[rustc_lint_diagnostics]
//~^ ERROR attribute should be applied to a function
struct Foo;

impl Foo {
    #[rustc_lint_diagnostics(a)]
    //~^ ERROR malformed `rustc_lint_diagnostics`
    fn bar() {}
}

fn main() {}


