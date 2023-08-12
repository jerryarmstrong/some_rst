tests/ui/suggestions/path-by-value.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::path::Path;

fn f(p: Path) { }
//~^ ERROR E0277

fn main() {}


