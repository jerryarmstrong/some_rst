tests/run-make-fulldeps/issue-18943/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo { }

trait Bar { }

impl<'a> Foo for Bar + 'a { }


