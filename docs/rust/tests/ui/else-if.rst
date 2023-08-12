tests/ui/else-if.rs
===================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    if 1 == 2 {
        assert!((false));
    } else if 2 == 3 {
        assert!((false));
    } else if 3 == 4 { assert!((false)); } else { assert!((true)); }
    if 1 == 2 { assert!((false)); } else if 2 == 2 { assert!((true)); }
    if 1 == 2 {
        assert!((false));
    } else if 2 == 2 {
        if 1 == 1 {
            assert!((true));
        } else { if 2 == 1 { assert!((false)); } else { assert!((false)); } }
    }
    if 1 == 2 {
        assert!((false));
    } else { if 1 == 2 { assert!((false)); } else { assert!((true)); } }
}


