tests/ui/coercion/coerce-block-tail-83783.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// edition:2018
fn _consume_reference<T: ?Sized>(_: &T) {}

async fn _foo() {
    _consume_reference::<i32>(&Box::new(7_i32));
    _consume_reference::<i32>(&async { Box::new(7_i32) }.await);
    //~^ ERROR mismatched types
    _consume_reference::<[i32]>(&vec![7_i32]);
    _consume_reference::<[i32]>(&async { vec![7_i32] }.await);
}

fn main() { }


