tests/ui/binop/binary-op-on-double-ref.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let vr = v.iter().filter(|x| {
        x % 2 == 0
        //~^ ERROR cannot mod `&&{integer}` by `{integer}`
    });
    println!("{:?}", vr);
}


