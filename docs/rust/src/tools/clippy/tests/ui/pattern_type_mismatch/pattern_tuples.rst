src/tools/clippy/tests/ui/pattern_type_mismatch/pattern_tuples.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::all)]
#![warn(clippy::pattern_type_mismatch)]

fn main() {}

fn tuple_types() {
    struct TupleStruct<'a>(&'a Option<i32>);
    let ref_value = &TupleStruct(&Some(42));

    // not ok
    let TupleStruct(_) = ref_value;
    if let &TupleStruct(Some(_)) = ref_value {}
    if let TupleStruct(Some(_)) = *ref_value {}

    // ok
    let &TupleStruct(_) = ref_value;
    let TupleStruct(_) = *ref_value;
    if let &TupleStruct(&Some(_)) = ref_value {}
    if let TupleStruct(&Some(_)) = *ref_value {}
}

fn tuple_enum_variants() {
    enum TupleEnum<'a> {
        Empty,
        Var(&'a Option<i32>),
    }
    let ref_value = &TupleEnum::Var(&Some(42));

    // not ok
    if let TupleEnum::Var(_) = ref_value {}
    if let &TupleEnum::Var(Some(_)) = ref_value {}
    if let TupleEnum::Var(Some(_)) = *ref_value {}
    if let TupleEnum::Empty = ref_value {}

    // ok
    if let &TupleEnum::Var(_) = ref_value {}
    if let TupleEnum::Var(_) = *ref_value {}
    if let &TupleEnum::Var(&Some(_)) = ref_value {}
    if let TupleEnum::Var(&Some(_)) = *ref_value {}
    if let &TupleEnum::Empty = ref_value {}
    if let TupleEnum::Empty = *ref_value {}
}

fn plain_tuples() {
    let ref_value = &(&Some(23), &Some(42));

    // not ok
    let (_a, _b) = ref_value;
    if let &(_a, Some(_)) = ref_value {}
    if let (_a, Some(_)) = *ref_value {}

    // ok
    let &(_a, _b) = ref_value;
    let (_a, _b) = *ref_value;
    if let &(_a, &Some(_)) = ref_value {}
    if let (_a, &Some(_)) = *ref_value {}
}


