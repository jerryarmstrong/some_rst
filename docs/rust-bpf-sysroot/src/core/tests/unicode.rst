src/core/tests/unicode.rs
=========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #[test]
pub fn version() {
    let (major, _minor, _update) = core::unicode::UNICODE_VERSION;
    assert!(major >= 10);
}


