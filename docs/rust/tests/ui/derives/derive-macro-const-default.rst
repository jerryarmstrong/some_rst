tests/ui/derives/derive-macro-const-default.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#[derive(Clone, PartialEq, Debug)]
struct Example<T, const N: usize = 1usize>([T; N]);

fn main() {
    let a = Example([(); 16]);
    let b = a.clone();
    if a != b {
        let _c = format!("{:?}", a);
    }
}


