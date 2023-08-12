src/core/tests/num/nan.rs
=========================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #[test]
fn test_nan() {
    let x = "NaN".to_string();
    assert_eq!(format!("{}", f64::NAN), x);
    assert_eq!(format!("{:e}", f64::NAN), x);
    assert_eq!(format!("{:E}", f64::NAN), x);
}


