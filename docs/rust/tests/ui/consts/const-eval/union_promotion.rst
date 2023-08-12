tests/ui/consts/const-eval/union_promotion.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(C)]
union Foo {
    a: &'static u32,
    b: usize,
}

fn main() {
    let x: &'static bool = &unsafe { //~ temporary value dropped while borrowed
        Foo { a: &1 }.b == Foo { a: &2 }.b
    };
}


