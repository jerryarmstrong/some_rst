tests/ui/test-attrs/run-unexported-tests.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// compile-flags:--test
// check-stdout

mod m {
    pub fn exported() {}

    #[test]
    fn unexported() {
        panic!("ran an unexported test");
    }
}


