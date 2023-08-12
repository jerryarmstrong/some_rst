tests/ui/repeat-expr/repeat-to-run-dtor-twice.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that one can't run a destructor twice with the repeated vector
// literal syntax.

struct Foo {
    x: isize,

}

impl Drop for Foo {
    fn drop(&mut self) {
        println!("Goodbye!");
    }
}

fn main() {
    let a = Foo { x: 3 };
    let _ = [ a; 5 ];
    //~^ ERROR the trait bound `Foo: Copy` is not satisfied [E0277]
}


