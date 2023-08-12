tests/ui/self/arbitrary_self_types_unsized_struct.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::rc::Rc;

struct Foo<T: ?Sized>(T);

impl Foo<[u8]> {
    fn len(self: Rc<Self>) -> usize {
        self.0.len()
    }
}

fn main() {
    let rc = Rc::new(Foo([1u8,2,3])) as Rc<Foo<[u8]>>;
    assert_eq!(3, rc.len());
}


