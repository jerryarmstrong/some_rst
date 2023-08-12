tests/rustdoc-ui/intra-doc/malformed-generics.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

//! [Vec<] //~ ERROR
//! [Vec<Box<T] //~ ERROR
//! [Vec<Box<T>] //~ ERROR
//~^ WARN
//! [Vec<Box<T>>>] //~ ERROR
//~^ WARN
//! [Vec<T>>>] //~ ERROR
//~^ WARN
//! [<Vec] //~ ERROR
//! [Vec::<] //~ ERROR
//! [<T>] //~ ERROR
//~^ WARN
//! [<invalid syntax>] //~ ERROR
//~^ WARN
//! [Vec:<T>:new()] //~ ERROR
//~^ WARN
//! [Vec<<T>>] //~ ERROR
//~^ WARN
//! [Vec<>] //~ ERROR
//! [Vec<<>>] //~ ERROR

// FIXME(#74563) support UFCS
//! [<Vec as IntoIterator>::into_iter] //~ ERROR
//~^ WARN
//! [<Vec<T> as IntoIterator>::iter] //~ ERROR
//~^ WARN


