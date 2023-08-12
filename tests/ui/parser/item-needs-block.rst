tests/ui/parser/item-needs-block.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait;
//~^ ERROR expected `{}`, found `;`

impl Trait for ();
//~^ ERROR expected `{}`, found `;`

enum Enum;
//~^ ERROR expected `{}`, found `;`

fn main() {}


