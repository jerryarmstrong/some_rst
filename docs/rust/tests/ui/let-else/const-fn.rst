tests/ui/let-else/const-fn.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// issue #101932


const fn foo(a: Option<i32>) -> i32 {
    let Some(a) = a else {
        return 42
    };

    a + 1
}

fn main() {
    const A: i32 = foo(None);
    const B: i32 = foo(Some(1));

    println!("{} {}", A, B);
}


