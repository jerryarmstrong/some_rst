tests/ui/issues/issue-5997-enum.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<Z>() -> bool {
    enum E { V(Z) }
    //~^ ERROR can't use generic parameters from outer function
    true
}

fn main() {
    let b = f::<isize>();
    assert!(b);
}


