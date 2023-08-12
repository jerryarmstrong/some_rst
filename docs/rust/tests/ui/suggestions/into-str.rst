tests/ui/suggestions/into-str.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<'a, T>(_t: T) where T: Into<&'a str> {}

fn main() {
    foo(String::new());
    //~^ ERROR the trait bound `&str: From<String>` is not satisfied
}


