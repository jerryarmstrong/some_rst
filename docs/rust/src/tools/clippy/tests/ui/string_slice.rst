src/tools/clippy/tests/ui/string_slice.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::string_slice)]
#[allow(clippy::no_effect)]

fn main() {
    &"Ölkanne"[1..];
    let m = "Mötörhead";
    &m[2..5];
    let s = String::from(m);
    &s[0..2];
}


