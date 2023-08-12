tests/ui/static/static-method-privacy.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub struct S;
    impl S {
        fn new() -> S { S }
    }
}

fn main() {
    let _ = a::S::new();    //~ ERROR associated function `new` is private
}


