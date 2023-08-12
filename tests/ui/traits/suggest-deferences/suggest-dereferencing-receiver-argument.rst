tests/ui/traits/suggest-deferences/suggest-dereferencing-receiver-argument.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

struct TargetStruct;

impl From<usize> for TargetStruct {
    fn from(_unchecked: usize) -> Self {
        TargetStruct
    }
}

fn main() {
    let a = &3;
    let _b: TargetStruct = a.into(); //~ ERROR the trait bound `TargetStruct: From<&{integer}>` is not satisfied
}


