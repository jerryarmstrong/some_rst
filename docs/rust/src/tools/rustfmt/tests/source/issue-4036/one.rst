src/tools/rustfmt/tests/source/issue-4036/one.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true

macro_rules! test {
    () => {
        fn from() {
            None.expect(
                "We asserted that `buffer.len()` is exactly `$n` so we can expect `ApInt::from_iter` to be successful.",
            )
        }
    };
}


