tests/ui/lint/force-warn/warnings-lint-group.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // --force-warn warnings is an error
// compile-flags: --force-warn warnings
// error-pattern: `warnings` lint group is not supported

fn main() {}


