tests/ui/associated-types/associated-types-in-inherent-method.rs
================================================================

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

impl Struct {
    fn grab<T:Get>(x: &T) -> &<T as Get>::Value {
        x.get()
    }
}

fn main() {
    let s = Struct {
        x: 100,
    };
    assert_eq!(*Struct::grab(&s), 100);
}


