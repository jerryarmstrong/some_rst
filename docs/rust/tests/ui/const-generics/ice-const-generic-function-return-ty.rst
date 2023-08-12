tests/ui/const-generics/ice-const-generic-function-return-ty.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #95163
fn return_ty() -> impl Into<<() as Reexported;
//~^ ERROR expected one of `(`, `::`, `<`, or `>`, found `;`

fn main() {}


