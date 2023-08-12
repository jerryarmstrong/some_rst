tests/ui/self/self-in-mut-slot-immediate-value.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Assert that `mut self` on an immediate value doesn't
// allow mutating the original - issue #10615.


#[derive(Copy, Clone)]
struct Value {
    n: isize
}

impl Value {
    fn squared(mut self) -> Value {
        self.n *= self.n;
        self
    }
}

pub fn main() {
    let x = Value { n: 3 };
    let y = x.squared();
    assert_eq!(x.n, 3);
    assert_eq!(y.n, 9);
}


