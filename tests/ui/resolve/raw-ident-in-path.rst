tests/ui/resolve/raw-ident-in-path.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #63882.

type A = crate::r#break; //~ ERROR cannot find type `r#break` in the crate root

fn main() {}


