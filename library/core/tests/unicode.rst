library/core/tests/unicode.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[test]
pub fn version() {
    let (major, _minor, _update) = core::char::UNICODE_VERSION;
    assert!(major >= 10);
}


