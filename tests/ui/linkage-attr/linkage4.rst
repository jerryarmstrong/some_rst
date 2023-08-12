tests/ui/linkage-attr/linkage4.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[linkage = "external"]
static foo: isize = 0;
//~^^ ERROR: the `linkage` attribute is experimental and not portable

fn main() {}


