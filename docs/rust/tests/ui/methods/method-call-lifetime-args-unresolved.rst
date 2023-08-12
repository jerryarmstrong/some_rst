tests/ui/methods/method-call-lifetime-args-unresolved.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    0.clone::<'a>();
    //~^ ERROR use of undeclared lifetime name `'a`
    //~| WARN cannot specify lifetime arguments explicitly if late bound
    //~| WARN this was previously accepted by the compiler
}


