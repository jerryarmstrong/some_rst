tests/ui/rfc-2008-non-exhaustive/enum_same_crate.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[non_exhaustive]
pub enum NonExhaustiveEnum {
    Unit,
    Tuple(u32),
    Struct { field: u32 }
}

fn main() {
    let enum_unit = NonExhaustiveEnum::Unit;

    match enum_unit {
        NonExhaustiveEnum::Unit => "first",
        NonExhaustiveEnum::Tuple(_) => "second",
        NonExhaustiveEnum::Struct { .. } => "third",
    };
}


