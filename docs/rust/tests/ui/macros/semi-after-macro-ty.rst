tests/ui/macros/semi-after-macro-ty.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! foo {
    ($t:ty; $p:path;) => {}
}

fn main() {
    foo!(i32; i32;);
}


