tests/ui/consts/issue-58435-ice-with-assoc-const.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// The const-evaluator was at one point ICE'ing while trying to
// evaluate the body of `fn id` during the `s.id()` call in main.

struct S<T>(T);

impl<T> S<T> {
    const ID: fn(&S<T>) -> &S<T> = |s| s;
    pub fn id(&self) -> &Self {
        Self::ID(self) // This, plus call below ...
    }
}

fn main() {
    let s = S(10u32);
    assert!(S::<u32>::ID(&s).0 == 10); // Works fine
    assert!(s.id().0 == 10); // ... causes compiler to panic
}


