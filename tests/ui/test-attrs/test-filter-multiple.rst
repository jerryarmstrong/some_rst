tests/ui/test-attrs/test-filter-multiple.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test
// run-flags: --test-threads=1 test1 test2
// check-run-results
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// ignore-emscripten no threads support

#[test]
fn test1() {}

#[test]
fn test2() {}

#[test]
fn test3() {
    panic!("this should not run");
}


