tests/mir-opt/76803_regression.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z mir-opt-level=1
// EMIT_MIR 76803_regression.encode.SimplifyBranchSame.diff

#[derive(Debug, Eq, PartialEq)]
pub enum Type {
    A,
    B,
}

pub fn encode(v: Type) -> Type {
    match v {
        Type::A => Type::B,
        _ => v,
    }
}

fn main() {
    assert_eq!(Type::B, encode(Type::A));
}


