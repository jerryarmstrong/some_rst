tests/ui/panics/default-backtrace-ice.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unset-rustc-env:RUST_BACKTRACE
// compile-flags:-Z treat-err-as-bug=1
// error-pattern:stack backtrace:
// failure-status:101
// normalize-stderr-test "note: .*" -> ""
// normalize-stderr-test "thread 'rustc' .*" -> ""
// normalize-stderr-test "  .*\n" -> ""

fn main() { missing_ident; }


