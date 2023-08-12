tests/ui/const-generics/generic_arg_infer/dont-use-defaults.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_arg_infer)]

// test that we dont use defaults to aide in type inference

struct Foo<const N: usize = 2>;
impl<const N: usize> Foo<N> {
    fn make_arr() -> [(); N] {
        [(); N]
    }
}

fn main() {
    let [(), (), ()] = Foo::<_>::make_arr();
}


