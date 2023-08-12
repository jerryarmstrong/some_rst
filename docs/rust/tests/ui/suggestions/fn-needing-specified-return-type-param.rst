tests/ui/suggestions/fn-needing-specified-return-type-param.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<A>() -> A { unimplemented!() }
fn foo() {
    let _ = f;
    //~^ ERROR type annotations needed
    //~| HELP consider specifying the generic argument
}
fn main() {}


