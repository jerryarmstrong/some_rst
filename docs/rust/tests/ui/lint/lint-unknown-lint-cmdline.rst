tests/ui/lint/lint-unknown-lint-cmdline.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-D bogus -D dead_cod

// error-pattern:unknown lint: `bogus`
// error-pattern:requested on the command line with `-D bogus`
// error-pattern:unknown lint: `dead_cod`
// error-pattern:requested on the command line with `-D dead_cod`
// error-pattern:did you mean: `dead_code`

fn main() { }


