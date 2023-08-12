tests/ui/const-generics/occurs-check/unused-substs-5.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// `N + 1` also depends on `T` here even if it doesn't use it.
fn q<T, const N: usize>(_: T) -> [u8; N + 1] {
    todo!()
}

fn supplier<T>() -> T {
    todo!()
}

fn catch_me<const N: usize>() where [u8; N + 1]: Default {
    let mut x = supplier();
    x = q::<_, N>(x); //~ ERROR mismatched types
}

fn main() {
    catch_me::<3>();
}


