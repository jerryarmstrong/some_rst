tests/ui/rfc-2008-non-exhaustive/enum_same_crate_empty_match.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

#[non_exhaustive]
pub enum NonExhaustiveEnum {
    Unit,
    //~^ not covered
    Tuple(u32),
    //~^ not covered
    Struct { field: u32 }
    //~^ not covered
}

pub enum NormalEnum {
    Unit,
    //~^ not covered
    Tuple(u32),
    //~^ not covered
    Struct { field: u32 }
    //~^ not covered
}

#[non_exhaustive]
pub enum EmptyNonExhaustiveEnum {}

fn empty_non_exhaustive(x: EmptyNonExhaustiveEnum) {
    match x {}
    match x {
        _ => {} //~ ERROR unreachable pattern
    }
}

fn main() {
    match NonExhaustiveEnum::Unit {}
    //~^ ERROR `NonExhaustiveEnum::Unit`, `NonExhaustiveEnum::Tuple(_)` and `NonExhaustiveEnum::Struct { .. }` not covered [E0004]
    match NormalEnum::Unit {}
    //~^ ERROR `NormalEnum::Unit`, `NormalEnum::Tuple(_)` and `NormalEnum::Struct { .. }` not covered [E0004]
}


