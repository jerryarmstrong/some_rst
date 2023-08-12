tests/ui/proc-macro/pretty-print-hack/rental-0.5.6/src/lib.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test

#[derive(Print)]
enum ProceduralMasqueradeDummyType {
//~^ ERROR using
//~| WARN this was previously
//~| ERROR using
//~| WARN this was previously
//~| ERROR using
//~| WARN this was previously
//~| ERROR using
//~| WARN this was previously
    Input
}


