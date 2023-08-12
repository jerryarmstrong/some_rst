src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0047_minus_in_inner_pattern.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust-analyzer/issues/972

fn main() {
    match Some(-1) {
        Some(-1) => (),
        _ => (),
    }

    match Some((-1, -1)) {
        Some((-1, -1)) => (),
        _ => (),
    }

    match A::B(-1, -1) {
        A::B(-1, -1) => (),
        _ => (),
    }

    if let Some(-1) = Some(-1) {
    }
}

enum A {
    B(i8, i8)
}

fn foo(-128..=127: i8) {}


