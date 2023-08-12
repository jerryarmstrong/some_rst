tests/ui/traits/wf-object/only-maybe-bound.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `dyn ?Sized` (i.e., a trait object with only a maybe buond) is not allowed.

type _0 = dyn ?Sized;
//~^ ERROR at least one trait is required for an object type [E0224]
//~| ERROR ?Trait` is not permitted in trait object types

fn main() {}


