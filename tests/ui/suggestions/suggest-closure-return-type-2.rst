tests/ui/suggestions/suggest-closure-return-type-2.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn unbound_drop(_: impl Sized) {}

fn main() {
    unbound_drop(|| { [] })
    //~^ ERROR type annotations needed for `[_; 0]`
    //~| HELP try giving this closure an explicit return type
}


