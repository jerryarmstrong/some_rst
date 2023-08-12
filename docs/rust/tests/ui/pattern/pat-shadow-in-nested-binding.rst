tests/ui/pattern/pat-shadow-in-nested-binding.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(non_camel_case_types)]
struct foo(usize);

fn main() {
    let (foo, _) = (2, 3); //~ ERROR let bindings cannot shadow tuple structs
}


