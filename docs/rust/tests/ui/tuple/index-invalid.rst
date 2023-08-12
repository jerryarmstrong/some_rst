tests/ui/tuple/index-invalid.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = (((),),).1.0; //~ ERROR no field `1` on type `(((),),)`

    let _ = (((),),).0.1; //~ ERROR no field `1` on type `((),)`

    let _ = (((),),).000.000; //~ ERROR no field `000` on type `(((),),)`
}


