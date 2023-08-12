tests/ui/match/match-on-negative-integer-ranges.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    assert_eq!(false, match -50_i8 { -128i8..=-101i8 => true, _ => false, });

    assert_eq!(false, if let -128i8..=-101i8 = -50_i8 { true } else { false });
}


