tests/ui/consts/const-eval/const_signed_pat.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    const MIN: i8 = -5;
    match 5i8 {
        MIN..=-1 => {},
        _ => {},
    }
}


