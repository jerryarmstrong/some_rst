tests/ui/unknown-tool-name.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[foo::bar] //~ ERROR failed to resolve: use of undeclared crate or module `foo`
fn main() {}


