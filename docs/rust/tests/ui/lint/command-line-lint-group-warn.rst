tests/ui/lint/command-line-lint-group-warn.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -W bad-style
// check-pass

fn main() {
    let _InappropriateCamelCasing = true;
    //~^ WARNING should have a snake case name
}


