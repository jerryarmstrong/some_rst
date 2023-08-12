tests/ui/modules/special_module_name.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod lib;
//~^ WARN found module declaration for lib.rs
//~| ERROR file not found for module `lib`
mod main;
//~^ WARN found module declaration for main.rs
//~| ERROR file not found for module `main`

fn main() {}


