src/tools/rust-analyzer/crates/parser/test_data/lexer/err/empty_int.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    0b
0o
0x

0b_
0o_
0x_

0bnoDigit
0onoDigit
0xnoDigit

0xG
0xg

0x_g
0x_G


