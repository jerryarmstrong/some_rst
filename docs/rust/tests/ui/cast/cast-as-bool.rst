tests/ui/cast/cast-as-bool.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let u = 5 as bool; //~ ERROR cannot cast as `bool`
                       //~| HELP compare with zero instead
                       //~| SUGGESTION 5 != 0

    let t = (1 + 2) as bool; //~ ERROR cannot cast as `bool`
                             //~| HELP compare with zero instead
                             //~| SUGGESTION (1 + 2) != 0

    let v = "hello" as bool;
    //~^ ERROR casting `&'static str` as `bool` is invalid
    //~| HELP consider using the `is_empty` method on `&'static str` to determine if it contains anything
}


