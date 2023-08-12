src/tools/rustfmt/tests/source/issue-3651.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> Box<
    dyn FnMut() -> Thing< WithType = LongItemName, Error = LONGLONGLONGLONGLONGONGEvenLongerErrorNameLongerLonger>,
>{
}

