tests/ui/codegen/issue-101585-128bit-repeat.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue 101585.
// run-pass

fn main() {
    fn min_array_ok() -> [i128; 1] {
        [i128::MIN]
    }
    assert_eq!(min_array_ok(), [-170141183460469231731687303715884105728i128]);

    fn min_array_nok() -> [i128; 1] {
        [i128::MIN; 1]
    }
    assert_eq!(min_array_nok(), [-170141183460469231731687303715884105728i128]);
}


