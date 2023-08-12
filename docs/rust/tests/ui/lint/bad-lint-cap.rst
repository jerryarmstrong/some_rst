tests/ui/lint/bad-lint-cap.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cap-lints test
// error-pattern: unknown lint level: `test`

fn main() {}


