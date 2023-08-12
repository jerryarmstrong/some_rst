tests/ui/parser/underscore-suffix-for-string.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! sink {
    ($tt:tt) => {()}
}

fn main() {
    let _ = "Foo"_;
    //~^ ERROR underscore literal suffix is not allowed

    // This is ok, because `__` is a valid identifier and the macro consumes it
    // before proper parsing happens.
    let _ = sink!("Foo"__);

    // This is not ok, even as an input to a macro, because the `_` suffix is
    // never allowed.
    sink!("Foo"_);
    //~^ ERROR underscore literal suffix is not allowed
}


