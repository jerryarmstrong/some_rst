tests/ui/cast/codegen-object-shim.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    assert_eq!((ToString::to_string as fn(&(dyn ToString+'static)) -> String)(&"foo"),
        String::from("foo"));
}


