tests/ui/closure_context/issue-26046-fn-once.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn get_closure() -> Box<dyn Fn() -> Vec<u8>> {
    let vec = vec![1u8, 2u8];

    let closure = move || { //~ ERROR expected a closure
        vec
    };

    Box::new(closure)
}

fn main() {}


