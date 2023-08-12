tests/ui/feature-gates/feature-gate-closure_lifetime_binder.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for<> || -> () {};
    //~^ ERROR `for<...>` binders for closures are experimental
    for<'a> || -> () {};
    //~^ ERROR `for<...>` binders for closures are experimental
    for<'a, 'b> |_: &'a ()| -> () {};
    //~^ ERROR `for<...>` binders for closures are experimental
}


