tests/ui/const-generics/defaults/const-param-in-ty-defaults.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo<const N: usize, T = [u8; N]>(T);

impl<const N: usize> Foo<N> {
    fn new() -> Self {
        Foo([0; N])
    }
}

fn main() {
    assert_eq!(Foo::new().0, [0; 10]);
}


