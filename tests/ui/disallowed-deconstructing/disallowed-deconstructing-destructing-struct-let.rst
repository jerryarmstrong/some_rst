tests/ui/disallowed-deconstructing/disallowed-deconstructing-destructing-struct-let.rs
======================================================================================

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

fn unwrap(x: X) -> String {
    let X { x: y } = x; //~ ERROR cannot move out of type
    y.to_string()
}

fn main() {
    let x = X { x: "hello".to_string() };
    let y = unwrap(x);
    println!("contents: {}", y);
}


