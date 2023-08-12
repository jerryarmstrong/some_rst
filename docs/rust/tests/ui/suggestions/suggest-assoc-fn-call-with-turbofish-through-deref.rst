tests/ui/suggestions/suggest-assoc-fn-call-with-turbofish-through-deref.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::RefCell;

struct HasAssocMethod;

impl HasAssocMethod {
    fn hello() {}
}
fn main() {
    let shared_state = RefCell::new(HasAssocMethod);
    let state = shared_state.borrow_mut();
    state.hello();
    //~^ ERROR no method named `hello` found
}


