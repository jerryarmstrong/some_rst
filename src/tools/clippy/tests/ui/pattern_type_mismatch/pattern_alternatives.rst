src/tools/clippy/tests/ui/pattern_type_mismatch/pattern_alternatives.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::all)]
#![warn(clippy::pattern_type_mismatch)]

fn main() {}

fn alternatives() {
    enum Value<'a> {
        Unused,
        A(&'a Option<i32>),
        B,
    }
    let ref_value = &Value::A(&Some(23));

    // not ok
    if let Value::B | Value::A(_) = ref_value {}
    if let &Value::B | &Value::A(Some(_)) = ref_value {}
    if let Value::B | Value::A(Some(_)) = *ref_value {}

    // ok
    if let &Value::B | &Value::A(_) = ref_value {}
    if let Value::B | Value::A(_) = *ref_value {}
    if let &Value::B | &Value::A(&Some(_)) = ref_value {}
    if let Value::B | Value::A(&Some(_)) = *ref_value {}
}


