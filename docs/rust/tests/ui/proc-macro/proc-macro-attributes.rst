tests/ui/proc-macro/proc-macro-attributes.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:derive-b.rs

#[macro_use]
extern crate derive_b;

#[B] //~ ERROR `B` is ambiguous
     //~| WARN derive helper attribute is used before it is introduced
     //~| WARN this was previously accepted
#[C] //~ ERROR cannot find attribute `C` in this scope
#[B(D)] //~ ERROR `B` is ambiguous
        //~| WARN derive helper attribute is used before it is introduced
        //~| WARN this was previously accepted
#[B(E = "foo")] //~ ERROR `B` is ambiguous
                //~| WARN derive helper attribute is used before it is introduced
                //~| WARN this was previously accepted
#[B(arbitrary tokens)] //~ ERROR `B` is ambiguous
                       //~| WARN derive helper attribute is used before it is introduced
                       //~| WARN this was previously accepted
#[derive(B)]
struct B;

fn main() {}


