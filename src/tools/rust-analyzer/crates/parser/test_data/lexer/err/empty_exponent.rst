src/tools/rust-analyzer/crates/parser/test_data/lexer/err/empty_exponent.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    0e
0E

42e+
42e-
42E+
42E-

42.e+
42.e-
42.E+
42.E-

42.2e+
42.2e-
42.2E+
42.2E-

42.2e+f32
42.2e-f32
42.2E+f32
42.2E-f32


