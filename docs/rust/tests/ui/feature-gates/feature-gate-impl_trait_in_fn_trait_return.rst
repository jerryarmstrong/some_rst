tests/ui/feature-gates/feature-gate-impl_trait_in_fn_trait_return.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> impl Fn() -> impl Sized { || () }
//~^ ERROR `impl Trait` only allowed in function and inherent method return types, not in `Fn` trait return
fn g() -> &'static dyn Fn() -> impl Sized { &|| () }
//~^ ERROR `impl Trait` only allowed in function and inherent method return types, not in `Fn` trait return

fn main() {}


