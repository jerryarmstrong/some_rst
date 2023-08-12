tests/ui/drop/drop-with-type-ascription-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let args = vec!["foobie", "asdf::asdf"];
    let arr: Vec<&str> = args[1].split("::").collect();
    assert_eq!(arr[0], "asdf");
    assert_eq!(arr[0], "asdf");
}


