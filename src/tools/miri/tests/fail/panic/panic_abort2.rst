src/tools/miri/tests/fail/panic/panic_abort2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: the program aborted execution
//@normalize-stderr-test: "\| +\^+" -> "| ^"
//@normalize-stderr-test: "libc::abort\(\);|core::intrinsics::abort\(\);" -> "ABORT();"
//@compile-flags: -C panic=abort

fn main() {
    std::panic!("{}-panicking from libstd", 42);
}


