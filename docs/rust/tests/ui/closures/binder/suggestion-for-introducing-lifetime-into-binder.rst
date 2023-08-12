tests/ui/closures/binder/suggestion-for-introducing-lifetime-into-binder.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(closure_lifetime_binder)]
fn main() {
    for<> |_: &'a ()| -> () {};
    //~^ ERROR use of undeclared lifetime name `'a`
    for<'a> |_: &'b ()| -> () {};
    //~^ ERROR use of undeclared lifetime name `'b`
}


