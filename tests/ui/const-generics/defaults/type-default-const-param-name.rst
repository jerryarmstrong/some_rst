tests/ui/const-generics/defaults/type-default-const-param-name.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
struct N;

struct Foo<const N: usize = 1, T = N>(T);

impl Foo {
    fn new() -> Self {
        Foo(N)
    }
}

fn main() {
    let Foo::<1, N>(N) = Foo::new();
}


