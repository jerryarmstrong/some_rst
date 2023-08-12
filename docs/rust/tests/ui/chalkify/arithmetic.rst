tests/ui/chalkify/arithmetic.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

fn main() {
    1 + 2;
    3 * 6;
    2 - 5;
    17 / 6;
    23 % 11;
    4 & 6;
    7 | 15;
    4 << 7;
    123 >> 3;
    1 == 2;
    5 != 5;
    6 < 2;
    7 > 11;
    3 <= 1;
    9 >= 14;
}


