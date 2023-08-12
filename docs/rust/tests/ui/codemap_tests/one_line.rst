tests/ui/codemap_tests/one_line.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut v = vec![Some("foo"), Some("bar")];
    v.push(v.pop().unwrap()); //~ ERROR cannot borrow
}


