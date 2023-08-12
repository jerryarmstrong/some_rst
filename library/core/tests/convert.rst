library/core/tests/convert.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[test]
fn convert() {
    const fn from(x: i32) -> i32 {
        i32::from(x)
    }

    const FOO: i32 = from(42);
    assert_eq!(FOO, 42);

    const fn into(x: Vec<String>) -> Vec<String> {
        x.into()
    }

    const BAR: Vec<String> = into(Vec::new());
    assert_eq!(BAR, Vec::<String>::new());
}


