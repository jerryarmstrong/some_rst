tests/ui/closures/closure-immutable-outer-variable.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

// Point at the captured immutable outer variable

fn foo(mut f: Box<dyn FnMut()>) {
    f();
}

fn main() {
    let y = true;
    foo(Box::new(move || y = !y) as Box<_>);
    //~^ ERROR cannot assign to `y`, as it is not declared as mutable
}


