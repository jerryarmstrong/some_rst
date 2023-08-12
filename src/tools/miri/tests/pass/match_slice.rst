src/tools/miri/tests/pass/match_slice.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = "hello";
    match x {
        "foo" => {}
        "bar" => {}
        _ => {}
    }
}


