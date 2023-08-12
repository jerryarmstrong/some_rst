tests/ui/foreign/issue-91370-foreign-fn-block-impl.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #91370.

extern {
    //~^ `extern` blocks define existing foreign functions
    fn f() {
        //~^ incorrect function inside `extern` block
        //~| cannot have a body
        impl Copy for u8 {}
    }
}

fn main() {}


