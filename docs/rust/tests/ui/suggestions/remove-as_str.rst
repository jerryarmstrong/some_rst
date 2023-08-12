tests/ui/suggestions/remove-as_str.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo1(s: &str) {
    s.as_str();
    //~^ ERROR no method named `as_str` found
}

fn foo2<'a>(s: &'a str) {
    s.as_str();
    //~^ ERROR no method named `as_str` found
}

fn foo3(s: &mut str) {
    s.as_str();
    //~^ ERROR no method named `as_str` found
}

fn foo4(s: &&str) {
    s.as_str();
    //~^ ERROR no method named `as_str` found
}

fn main() {}


