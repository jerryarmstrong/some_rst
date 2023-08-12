tests/ui/macros/macro-2.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {

    macro_rules! mylambda_tt {
        ($x:ident, $body:expr) => ({
            fn f($x: isize) -> isize { return $body; }
            f
        })
    }

    assert_eq!(mylambda_tt!(y, y * 2)(8), 16);
}


