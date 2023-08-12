src/tools/miri/tests/pass/issues/issue-miri-1075.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let f: fn() -> ! = || std::process::exit(0);
    f();

    // FIXME: Also add a test for <https://github.com/rust-lang/rust/issues/66738>, once that is fixed.
}


