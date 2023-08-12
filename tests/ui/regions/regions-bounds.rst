tests/ui/regions/regions-bounds.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that explicit region bounds are allowed on the various
// nominal types (but not on other types) and that they are type
// checked.

struct TupleStruct<'a>(&'a isize);
struct Struct<'a> { x:&'a isize }

fn a_fn1<'a,'b>(e: TupleStruct<'a>) -> TupleStruct<'b> {
    return e;
    //~^ ERROR lifetime may not live long enough
}

fn a_fn3<'a,'b>(e: Struct<'a>) -> Struct<'b> {
    return e;
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


