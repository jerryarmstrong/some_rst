src/tools/rustfmt/tests/target/closure-block-inside-macro.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #1547
fuzz_target!(|data: &[u8]| if let Some(first) = data.first() {
    let index = *first as usize;
    if index >= ENCODINGS.len() {
        return;
    }
    let encoding = ENCODINGS[index];
    dispatch_test(encoding, &data[1..]);
});


