src/tools/rust-analyzer/crates/parser/test_data/lexer/ok/numbers.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    0 00 0_ 0. 0z
01790 0b1790 0o1790 0x1790aAbBcCdDeEfF 001279 0_1279 0.1279 0e1279 0E1279
0..2
0.foo()
0e+1
0.e+1
0.0E-2
0___0.10000____0000e+111__
1i64 92.0f32 11__s


