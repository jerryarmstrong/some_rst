tests/ui/test-attrs/inaccessible-test-modules.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test

// the `--test` harness creates modules with these textual names, but
// they should be inaccessible from normal code.
use main as x; //~ ERROR unresolved import `main`
use test as y; //~ ERROR unresolved import `test`

#[test]
fn baz() {}


