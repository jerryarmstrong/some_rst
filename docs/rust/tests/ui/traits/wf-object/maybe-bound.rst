tests/ui/traits/wf-object/maybe-bound.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `dyn ... + ?Sized + ...` is okay (though `?Sized` has no effect in trait objects).

trait Foo {}

type _0 = dyn ?Sized + Foo;
//~^ ERROR `?Trait` is not permitted in trait object types

type _1 = dyn Foo + ?Sized;
//~^ ERROR `?Trait` is not permitted in trait object types

type _2 = dyn Foo + ?Sized + ?Sized;
//~^ ERROR `?Trait` is not permitted in trait object types
//~| ERROR `?Trait` is not permitted in trait object types

type _3 = dyn ?Sized + Foo;
//~^ ERROR `?Trait` is not permitted in trait object types

fn main() {}


