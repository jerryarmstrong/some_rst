tests/ui/traits/do-not-mention-type-params-by-name-in-suggestion-issue-96292.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Thing<X>(X);

trait Method<T> {
    fn method(self, _: i32) -> T;
}

impl<X> Method<i32> for Thing<X> {
    fn method(self, _: i32) -> i32 { 0 }
}

impl<X> Method<u32> for Thing<X> {
    fn method(self, _: i32) -> u32 { 0 }
}

fn main() {
    let thing = Thing(true);
    thing.method(42);
    //~^ ERROR type annotations needed
    //~| ERROR type annotations needed
}


