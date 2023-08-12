src/tools/rustfmt/tests/source/nestedmod/mod.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    
mod mod2a;
mod mod2b;

mod mymod1 {
          use mod2a::{Foo,Bar};
mod mod3a;
}

#[path="mod2c.rs"]
mod mymod2;

mod submod2;


