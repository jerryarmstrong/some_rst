tests/ui/closure_context/issue-26046-fn-mut.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> Box<dyn Fn()> {
    let num = 5;

    let closure = || { //~ ERROR expected a closure that
        num += 1;
    };

    Box::new(closure)
}

fn main() {}


