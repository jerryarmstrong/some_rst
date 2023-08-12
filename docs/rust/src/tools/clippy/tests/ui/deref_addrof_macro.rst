src/tools/clippy/tests/ui/deref_addrof_macro.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! m {
    ($($x:tt),*) => { &[$(($x, stringify!(x)),)*] };
}

#[warn(clippy::deref_addrof)]
fn f() -> [(i32, &'static str); 3] {
    *m![1, 2, 3] // should be fine
}

fn main() {}


