tests/ui/pattern/usefulness/issue-4321.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let tup = (true, true);
    println!("foo {:}", match tup { //~ ERROR non-exhaustive patterns: `(true, false)` not covered
        (false, false) => "foo",
        (false, true) => "bar",
        (true, true) => "baz"
    });
}


