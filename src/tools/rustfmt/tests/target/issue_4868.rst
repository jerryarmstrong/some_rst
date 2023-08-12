src/tools/rustfmt/tests/target/issue_4868.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum NonAscii {
    Abcd,
    Éfgh,
}

use NonAscii::*;

fn f(x: NonAscii) -> bool {
    match x {
        Éfgh => true,
        _ => false,
    }
}

fn main() {
    dbg!(f(Abcd));
}


