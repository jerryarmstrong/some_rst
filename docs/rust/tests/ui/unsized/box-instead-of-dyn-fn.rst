tests/ui/unsized/box-instead-of-dyn-fn.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

// Test to suggest boxing the return type, and the closure branch of the `if`

fn print_on_or_the_other<'a>(a: i32, b: &'a String) -> dyn Fn() + 'a {
    //~^ ERROR return type cannot have an unboxed trait object
    if a % 2 == 0 {
        move || println!("{a}")
    } else {
        Box::new(move || println!("{}", b))
        //~^ ERROR `if` and `else` have incompatible types
    }
}

fn main() {}


