tests/ui/modules/path-invalid-form.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[path = 123]  //~ ERROR malformed `path` attribute
mod foo;

fn main() {}


