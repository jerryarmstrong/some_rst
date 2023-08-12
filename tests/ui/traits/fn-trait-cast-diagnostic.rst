tests/ui/traits/fn-trait-cast-diagnostic.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // There are two different instances to check that even if
// the trait is implemented for the output of a function,
// it will still be displayed if the function itself implements a trait.
trait Foo {}

impl Foo for fn() -> bool {}
impl Foo for bool {}

fn example() -> bool {
    true
}

trait NoOtherFoo {}

impl NoOtherFoo for fn() -> bool {}

fn do_on_foo(v: impl Foo) {}
fn do_on_single_foo(v: impl NoOtherFoo) {}

fn main() {
    do_on_foo(example);
    //~^ ERROR the trait bound

    do_on_single_foo(example);
    //~^ ERROR the trait bound
}


