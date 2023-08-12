tests/ui/deprecation/try-macro-suggestion.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018
fn foo() -> Result<(), ()> {
    Ok(try!()); //~ ERROR use of deprecated `try` macro
    Ok(try!(Ok(()))) //~ ERROR use of deprecated `try` macro
}

fn main() {
    let _ = foo();
}


