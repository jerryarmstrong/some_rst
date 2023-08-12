tests/ui/imports/import.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use zed::bar;
use zed::baz; //~ ERROR unresolved import `zed::baz` [E0432]
              //~| no `baz` in `zed`
              //~| HELP a similar name exists in the module
              //~| SUGGESTION bar


mod zed {
    pub fn bar() { println!("bar"); }
    use foo; //~ ERROR unresolved import `foo` [E0432]
             //~^ no `foo` in the root
}

fn main() {
    zed::foo(); //~ ERROR `foo` is private
    bar();
}


