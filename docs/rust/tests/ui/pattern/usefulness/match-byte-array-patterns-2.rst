tests/ui/pattern/usefulness/match-byte-array-patterns-2.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let buf = &[0, 1, 2, 3];

    match buf { //~ ERROR non-exhaustive
        b"AAAA" => {}
    }

    let buf: &[u8] = buf;

    match buf { //~ ERROR non-exhaustive
        b"AAAA" => {}
    }
}


