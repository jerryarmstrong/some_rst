src/tools/rustfmt/tests/source/negative-impl.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl ! Display for JoinHandle { }

impl ! Box < JoinHandle > { }

impl ! std :: fmt :: Display for JoinHandle < T : std :: future :: Future + std :: marker :: Send + std :: marker :: Sync > { }

impl ! JoinHandle < T : std :: future :: Future < Output > + std :: marker :: Send + std :: marker :: Sync + 'static > + 'static { }


