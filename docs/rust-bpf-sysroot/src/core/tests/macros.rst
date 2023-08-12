src/core/tests/macros.rs
========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #[test]
fn assert_eq_trailing_comma() {
    assert_eq!(1, 1,);
}

#[test]
fn assert_escape() {
    assert!(r#"☃\backslash"#.contains("\\"));
}

#[test]
fn assert_ne_trailing_comma() {
    assert_ne!(1, 2,);
}


