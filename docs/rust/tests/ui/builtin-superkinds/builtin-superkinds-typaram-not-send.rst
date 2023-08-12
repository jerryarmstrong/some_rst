tests/ui/builtin-superkinds/builtin-superkinds-typaram-not-send.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Basic test for traits inheriting from the builtin kinds.

trait Foo : Send { }

impl <T: Sync+'static> Foo for T { }
//~^ ERROR `T` cannot be sent between threads safely

fn main() { }


