tests/ui/test-attrs/test-runner-hides-main.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:--test
// Building as a test runner means that a synthetic main will be run,
// not ours
pub fn main() { panic!(); }


