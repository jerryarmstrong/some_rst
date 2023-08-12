tests/ui/extern/extern-macro.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #41719

fn main() {
    enum Foo {}
    let _ = Foo::bar!(); //~ ERROR failed to resolve: partially resolved path in a macro
}


