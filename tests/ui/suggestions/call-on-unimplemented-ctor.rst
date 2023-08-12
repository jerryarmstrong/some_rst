tests/ui/suggestions/call-on-unimplemented-ctor.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    insert_resource(Marker);
    insert_resource(Time);
    //~^ ERROR the trait bound `fn(u32) -> Time {Time}: Resource` is not satisfied
    //~| HELP use parentheses to construct this tuple struct
}

trait Resource {}

fn insert_resource<R: Resource>(resource: R) {}

struct Marker;
impl Resource for Marker {}

struct Time(u32);

impl Resource for Time {}


