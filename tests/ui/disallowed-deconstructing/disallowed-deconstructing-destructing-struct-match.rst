tests/ui/disallowed-deconstructing/disallowed-deconstructing-destructing-struct-match.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
struct X {
    x: String,
}

impl Drop for X {
    fn drop(&mut self) {
        println!("value: {}", self.x);
    }
}

fn main() {
    let x = X { x: "hello".to_string() };

    match x {
    //~^ ERROR cannot move out of type `X`, which implements the `Drop` trait
        X { x: y } => println!("contents: {}", y)
    }
}


