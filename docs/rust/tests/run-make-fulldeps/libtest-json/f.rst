tests/run-make-fulldeps/libtest-json/f.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[test]
fn a() {
    println!("print from successful test");
    // Should pass
}

#[test]
fn b() {
    assert!(false);
}

#[test]
#[should_panic]
fn c() {
    assert!(false);
}

#[test]
#[ignore = "msg"]
fn d() {
    assert!(false);
}


