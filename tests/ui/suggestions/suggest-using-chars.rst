tests/ui/suggestions/suggest-using-chars.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let _ = "foo".iter(); //~ ERROR no method named `iter` found for reference `&'static str` in the current scope
    let _ = "foo".foo(); //~ ERROR no method named `foo` found for reference `&'static str` in the current scope
    let _ = String::from("bar").iter(); //~ ERROR no method named `iter` found for struct `String` in the current scope
    let _ = (&String::from("bar")).iter(); //~ ERROR no method named `iter` found for reference `&String` in the current scope
    let _ = 0.iter(); //~ ERROR no method named `iter` found for type `{integer}` in the current scope
}


