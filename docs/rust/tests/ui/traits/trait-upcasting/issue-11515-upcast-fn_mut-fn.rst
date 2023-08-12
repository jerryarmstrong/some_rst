tests/ui/traits/trait-upcasting/issue-11515-upcast-fn_mut-fn.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(trait_upcasting)]

struct Test {
    func: Box<dyn FnMut() + 'static>,
}

fn main() {
    let closure: Box<dyn Fn() + 'static> = Box::new(|| ());
    let mut test = Box::new(Test { func: closure });
    (test.func)();
}


