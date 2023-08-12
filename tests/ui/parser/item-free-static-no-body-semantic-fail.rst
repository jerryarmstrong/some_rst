tests/ui/parser/item-free-static-no-body-semantic-fail.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Semantically, a free `static` item cannot omit its body.

fn main() {}

static A: u8; //~ ERROR free static item without body
static B; //~ ERROR free static item without body
//~^ ERROR missing type for `static` item

static mut C: u8; //~ ERROR free static item without body
static mut D; //~ ERROR free static item without body
//~^ ERROR missing type for `static mut` item


