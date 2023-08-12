library/core/tests/macros.rs
============================

Last edited: 2023-03-30 20:35:59

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

#[rustfmt::skip]
#[test]
fn matches_leading_pipe() {
    matches!(1, | 1 | 2 | 3);
}


