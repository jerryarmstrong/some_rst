tests/ui/suggestions/type-not-found-in-adt-field.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct {
    m: Vec<Someunknownname<String, ()>>, //~ ERROR cannot find type `Someunknownname` in this scope
    //~^ NOTE not found in this scope
}
struct OtherStruct { //~ HELP you might be missing a type parameter
    m: K, //~ ERROR cannot find type `K` in this scope
    //~^ NOTE not found in this scope
}
fn main() {}


