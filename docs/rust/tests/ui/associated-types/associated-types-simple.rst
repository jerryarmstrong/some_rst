tests/ui/associated-types/associated-types-simple.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Get {
    type Value;
    fn get(&self) -> &<Self as Get>::Value;
}

struct Struct {
    x: isize,
}

impl Get for Struct {
    type Value = isize;
    fn get(&self) -> &isize {
        &self.x
    }
}

fn main() {
    let s = Struct {
        x: 100,
    };
    assert_eq!(*s.get(), 100);
}


