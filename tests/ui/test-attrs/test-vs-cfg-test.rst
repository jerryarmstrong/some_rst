tests/ui/test-attrs/test-vs-cfg-test.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --cfg test

// Make sure `--cfg test` does not inject test harness

#[test]
fn test() { panic!(); }

fn main() {}


