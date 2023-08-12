tests/ui/issues/auxiliary/issue-9123.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub trait X {
    fn x() {
        fn f() { }
        f();
    }
    fn dummy(&self) { }
}


