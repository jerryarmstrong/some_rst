tests/mir-opt/uninhabited_enum_branching2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Empty { }

// test matching an enum with uninhabited variants
enum Test1 {
    A(Empty),
    B(Empty),
    C,
    D,
}

struct Plop {
    xx: u32,
    test1: Test1,
}

// EMIT_MIR uninhabited_enum_branching2.main.UninhabitedEnumBranching.diff
// EMIT_MIR uninhabited_enum_branching2.main.SimplifyCfg-after-uninhabited-enum-branching.after.mir
fn main() {
    let plop = Plop { xx: 51, test1: Test1::C };

    match &plop.test1 {
        Test1::A(_) => "A(Empty)",
        Test1::B(_) => "B(Empty)",
        Test1::C => "C",
        Test1::D => "D",
    };

    match plop.test1 {
        Test1::A(_) => "A(Empty)",
        Test1::B(_) => "B(Empty)",
        Test1::C => "C",
        Test1::D => "D",
    };
}


