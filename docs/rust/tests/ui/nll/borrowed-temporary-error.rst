tests/ui/nll/borrowed-temporary-error.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn gimme(x: &(u32,)) -> &u32 {
    &x.0
}

fn main() {
    let x = gimme({
        let v = 22;
        &(v,)
        //~^ ERROR temporary value dropped while borrowed [E0716]
    });
    println!("{:?}", x);
}


