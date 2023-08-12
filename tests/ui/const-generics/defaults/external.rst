tests/ui/const-generics/defaults/external.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:const_defaulty.rs
// check-pass
extern crate const_defaulty;
use const_defaulty::Defaulted;

struct Local<const N: usize=4>;
impl Local {
    fn new() -> Self {
        Local
    }
}
impl<const N: usize>Local<N> {
    fn value(&self) -> usize {
        N
    }
}

fn main() {
    let v = Defaulted::new();
    assert_eq!(v.value(), 3);

    let l = Local::new();
    assert_eq!(l.value(), 4);
}


