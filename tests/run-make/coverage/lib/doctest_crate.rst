tests/run-make/coverage/lib/doctest_crate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// A function run only from within doctests
pub fn fn_run_in_doctests(conditional: usize) {
    match conditional {
        1 => assert_eq!(1, 1), // this is run,
        2 => assert_eq!(1, 1), // this,
        3 => assert_eq!(1, 1), // and this too
        _ => assert_eq!(1, 2), // however this is not
    }
}


