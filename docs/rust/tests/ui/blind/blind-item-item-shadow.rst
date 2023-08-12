tests/ui/blind/blind-item-item-shadow.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo { pub mod foo {  } }

use foo::foo;
//~^ ERROR the name `foo` is defined multiple times
//~| `foo` reimported here

fn main() {}


