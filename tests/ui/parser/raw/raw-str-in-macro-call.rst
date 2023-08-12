tests/ui/parser/raw/raw-str-in-macro-call.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! m1 {
    ($tt:tt #) => ()
}

macro_rules! m2 {
    ($tt:tt) => ()
}

fn main() {
    m1!(r#"abc"##);
    m2!(r#"abc"#);
}


