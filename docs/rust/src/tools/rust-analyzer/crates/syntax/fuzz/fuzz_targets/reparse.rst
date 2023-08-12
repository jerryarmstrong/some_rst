src/tools/rust-analyzer/crates/syntax/fuzz/fuzz_targets/reparse.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Fuzzing for incremental parsing.

#![no_main]
use libfuzzer_sys::fuzz_target;
use syntax::fuzz::CheckReparse;

fuzz_target!(|data: &[u8]| {
    if let Some(check) = CheckReparse::from_data(data) {
        check.run();
    }
});


