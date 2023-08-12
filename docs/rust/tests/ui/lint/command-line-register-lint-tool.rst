tests/ui/lint/command-line-register-lint-tool.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -A known_tool::foo
// check-pass

#![feature(register_tool)]
#![register_tool(known_tool)]

fn main() {}


