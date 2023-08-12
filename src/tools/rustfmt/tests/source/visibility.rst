src/tools/rustfmt/tests/source/visibility.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #2398
pub mod outer_mod {
    pub mod inner_mod {
       pub ( in outer_mod ) fn outer_mod_visible_fn() {}
         pub ( super ) fn super_mod_visible_fn() {}
      pub ( self ) fn inner_mod_visible_fn() {}
    }
}


