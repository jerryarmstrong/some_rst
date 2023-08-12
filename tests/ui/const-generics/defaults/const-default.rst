tests/ui/const-generics/defaults/const-default.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub struct ConstDefault<const N: usize = 3>;

impl<const N: usize> ConstDefault<N> {
    fn foo(self) -> usize {
        N
    }
}

impl ConstDefault {
    fn new() -> Self {
        ConstDefault
    }

    fn bar(self) {}
}

pub fn main() {
    let s = ConstDefault::new();
    assert_eq!(s.foo(), 3);

    let w = ConstDefault::<3>;
    w.bar();
}


