tests/ui/macros/meta-item-absolute-path.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(::Absolute)] //~ ERROR failed to resolve
                      //~| ERROR failed to resolve
struct S;

fn main() {}


