tests/ui/const-generics/early/const-param-hygiene.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

macro_rules! bar {
    ($($t:tt)*) => { impl<const N: usize> $($t)* };
}

macro_rules! baz {
    ($t:tt) => { fn test<const M: usize>(&self) -> usize { $t } };
}

struct Foo<const N: usize>;

bar!(Foo<N> { baz!{ M } });

fn main() {
    assert_eq!(Foo::<7>.test::<3>(), 3);
}


