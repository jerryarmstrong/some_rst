tests/ui/nll/borrowed-local-error.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn gimme(x: &(u32,)) -> &u32 {
    &x.0
}

fn main() {
    let x = gimme({
        let v = (22,);
        &v
        //~^ ERROR `v` does not live long enough [E0597]
    });
    println!("{:?}", x);
}


