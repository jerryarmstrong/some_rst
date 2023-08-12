tests/ui/parser/doc-comment-in-stmt.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> bool {
    false
    //!self.allow_ty_infer()
    //~^ ERROR found doc comment
}

fn bar() -> bool {
    false
    /*! bar */ //~ ERROR found doc comment
}

fn baz() -> i32 {
    1 /** baz */ //~ ERROR found doc comment
}

fn quux() -> i32 {
    2 /*! quux */ //~ ERROR found doc comment
}

fn main() {}


