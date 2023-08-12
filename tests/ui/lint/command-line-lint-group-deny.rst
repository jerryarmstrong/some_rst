tests/ui/lint/command-line-lint-group-deny.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -D bad-style

fn main() {
    let _InappropriateCamelCasing = true; //~ ERROR should have a snake
}


