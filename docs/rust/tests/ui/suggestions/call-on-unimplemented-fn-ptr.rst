tests/ui/suggestions/call-on-unimplemented-fn-ptr.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

trait Bar {}

impl Bar for Foo {}

fn needs_bar<T: Bar>(_: T) {}

fn blah(f: fn() -> Foo) {
    needs_bar(f);
    //~^ ERROR the trait bound `fn() -> Foo: Bar` is not satisfied
    //~| HELP use parentheses to call this function pointer
}

fn main() {}


