tests/ui/const-generics/issues/issue-70273-assoc-fn.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait T<const A: usize> {
    fn f();
}
struct S;

impl T<0usize> for S {
    fn f() {}
}

fn main() {
    let _err = <S as T<0usize>>::f();
}


