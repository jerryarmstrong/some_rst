tests/ui/parser/item-free-const-no-body-semantic-fail.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Semantically, a free `const` item cannot omit its body.

fn main() {}

const A: u8; //~ ERROR free constant item without body
const B; //~ ERROR free constant item without body
//~^ ERROR missing type for `const` item


