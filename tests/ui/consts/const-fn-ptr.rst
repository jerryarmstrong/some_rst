tests/ui/consts/const-fn-ptr.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const fn make_fn_ptr() -> fn() {
    || {}
}

static STAT: () = make_fn_ptr()();
//~^ ERROR function pointer

const CONST: () = make_fn_ptr()();
//~^ ERROR function pointer

const fn call_ptr() {
    make_fn_ptr()();
    //~^ ERROR function pointer
}

fn main() {}


