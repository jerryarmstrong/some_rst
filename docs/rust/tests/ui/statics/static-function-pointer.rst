tests/ui/statics/static-function-pointer.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(x: isize) -> isize { x }
fn g(x: isize) -> isize { 2 * x }

static F: fn(isize) -> isize = f;
static mut G: fn(isize) -> isize = f;

pub fn main() {
    assert_eq!(F(42), 42);
    unsafe {
        assert_eq!(G(42), 42);
        G = g;
        assert_eq!(G(42), 84);
    }
}


