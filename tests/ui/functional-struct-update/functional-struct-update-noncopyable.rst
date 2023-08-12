tests/ui/functional-struct-update/functional-struct-update-noncopyable.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue 7327

use std::sync::Arc;

struct A { y: Arc<isize>, x: Arc<isize> }

impl Drop for A {
    fn drop(&mut self) { println!("x={}", *self.x); }
}
fn main() {
    let a = A { y: Arc::new(1), x: Arc::new(2) };
    let _b = A { y: Arc::new(3), ..a }; //~ ERROR cannot move out of type `A`
    let _c = a;
}


