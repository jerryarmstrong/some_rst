tests/ui/suggestions/type-ascription-instead-of-let.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn fun(x: i32) -> i32 { x }

fn main() {
    let closure_annotated = |value: i32| -> i32 {
        temp: i32 = fun(5i32);
        //~^ ERROR cannot find value `temp` in this scope
        temp + value + 1
        //~^ ERROR cannot find value `temp` in this scope
    };
}


