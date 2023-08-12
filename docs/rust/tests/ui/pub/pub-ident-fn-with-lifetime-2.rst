tests/ui/pub/pub-ident-fn-with-lifetime-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub   bar<'a>(&self, _s: &'a usize) -> bool { true }
//~^ ERROR missing `fn` for method definition

fn main() {
    bar(2);
}


