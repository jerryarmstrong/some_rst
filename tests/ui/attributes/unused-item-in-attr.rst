tests/ui/attributes/unused-item-in-attr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[w = { extern crate alloc; }]
//~^ ERROR unexpected expression: `{
//~| ERROR cannot find attribute `w` in this scope
fn f() {}

fn main() {}


