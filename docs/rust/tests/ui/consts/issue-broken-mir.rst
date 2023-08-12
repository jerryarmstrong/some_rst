tests/ui/consts/issue-broken-mir.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// https://github.com/rust-lang/rust/issues/27918

fn main() {
    match b"    " {
        b"1234" => {},
        _ => {},
    }
}


