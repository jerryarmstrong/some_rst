tests/ui/builtin-superkinds/builtin-superkinds-double-superkind.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for traits that inherit from multiple builtin kinds at once,
// testing that all such kinds must be present on implementing types.

trait Foo : Send+Sync { }

impl <T: Sync+'static> Foo for (T,) { }
//~^ ERROR `T` cannot be sent between threads safely [E0277]

impl <T: Send> Foo for (T,T) { }
//~^ ERROR `T` cannot be shared between threads safely [E0277]

impl <T: Send+Sync> Foo for (T,T,T) { } // (ok)

fn main() { }


