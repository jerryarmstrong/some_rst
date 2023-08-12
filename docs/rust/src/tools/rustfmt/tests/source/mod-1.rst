src/tools/rustfmt/tests/source/mod-1.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Deeply indented modules.

  mod foo { mod bar { mod baz {} } }

mod foo {
    mod bar {
    mod baz {
    fn foo() { bar() }
    }
    }

    mod qux {

    }
}

mod boxed { pub use std::boxed::{Box, HEAP}; }

pub  mod x {
        pub fn freopen(filename: *const c_char,
                   mode: *const c_char,
                     mode2: *const c_char,
                   mode3: *const c_char,
                   file: *mut FILE)
                   -> *mut FILE{}
}

  mod    y    { // sup boooooiiii
   }


