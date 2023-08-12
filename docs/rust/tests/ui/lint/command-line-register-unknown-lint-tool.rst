tests/ui/lint/command-line-register-unknown-lint-tool.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -A unknown_tool::foo
// error-pattern: unknown lint tool: `unknown_tool`

fn main() {}


