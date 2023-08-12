src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0058_range_pat.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 92 {
        0 ... 100 => (),
        101 ..= 200 => (),
        200 .. 301 => (),
        302 .. => (),
        ..= 303 => (),
    }

    match Some(10 as u8) {
        Some(0) | None => (),
        Some(1..) => (),
        Some(..=2) => (),
    }

    match () {
        S { a: 0 } => (),
        S { a: 1.. } => (),
        S { a: ..=2 } => (),
    }

    match () {
        [0] => (),
        [1..] => (),
        [..=2] => (),
    }

    match (10 as u8, 5 as u8) {
        (0, _) => (),
        (1.., _) => (),
        (..=2, _) => (),
    }
}


