tests/ui/autoref-autoderef/auto-ref-sliceable.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


trait Pushable<T> {
    fn push_val(&mut self, t: T);
}

impl<T> Pushable<T> for Vec<T> {
    fn push_val(&mut self, t: T) {
        self.push(t);
    }
}

pub fn main() {
    let mut v = vec![1];
    v.push_val(2);
    v.push_val(3);
    assert_eq!(v, [1, 2, 3]);
}


