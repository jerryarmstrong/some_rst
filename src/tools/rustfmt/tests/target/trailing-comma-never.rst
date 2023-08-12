src/tools/rustfmt/tests/target/trailing-comma-never.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-trailing_comma: Never

enum X {
    A,
    B
}

enum Y {
    A,
    B
}

enum TupX {
    A(u32),
    B(i32, u16)
}

enum TupY {
    A(u32),
    B(i32, u16)
}

enum StructX {
    A { s: u16 },
    B { u: u32, i: i32 }
}

enum StructY {
    A { s: u16 },
    B { u: u32, i: i32 }
}

static XXX: [i8; 64] = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
];


