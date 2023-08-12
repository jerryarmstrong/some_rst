tests/ui/proc-macro/empty-where-clause.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

extern crate test_macros;
use test_macros::recollect_attr;

#[recollect_attr]
struct FieldStruct where {
    field: MissingType1 //~ ERROR cannot find
}

#[recollect_attr]
struct TupleStruct(MissingType2) where; //~ ERROR cannot find

enum MyEnum where {
    Variant(MissingType3) //~ ERROR cannot find
}

fn main() {}


