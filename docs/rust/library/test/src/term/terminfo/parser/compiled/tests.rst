library/test/src/term/terminfo/parser/compiled/tests.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::*;

#[test]
fn test_veclens() {
    assert_eq!(boolfnames.len(), boolnames.len());
    assert_eq!(numfnames.len(), numnames.len());
    assert_eq!(stringfnames.len(), stringnames.len());
}


