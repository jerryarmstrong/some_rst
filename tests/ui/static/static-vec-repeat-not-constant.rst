tests/ui/static/static-vec-repeat-not-constant.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> isize { 23 }

static a: [isize; 2] = [foo(); 2];
//~^ ERROR: E0015

fn main() {}


